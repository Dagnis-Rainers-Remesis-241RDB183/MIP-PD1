from pathlib import Path
from typing import Any

from src.computer import Computer

from .game import Game


class ExperimentGame(Game):
    fixed_numbers: list[int]
    log_path: Path
    pending_ai_report: dict[str, Any] | None
    result_logged: bool
    ai_move_count: int
    total_generated_vertices: int
    total_evaluated_vertices: int
    total_move_time: float
    use_fixed_numbers: bool

    def __init__(self, log_path: str = "test_logs.txt") -> None:
        super().__init__()
        self.fixed_numbers = [6, 1, 4, 6, 4, 6, 2, 2, 2, 3, 3, 3, 5, 3, 3]
        self.log_path = Path(log_path)
        self.pending_ai_report = None
        self.result_logged = False
        self.ai_move_count = 0
        self.total_generated_vertices = 0
        self.total_evaluated_vertices = 0
        self.total_move_time = 0.0
        self.use_fixed_numbers = True

    def start(
        self,
        number_count: int,
        level: int,
        player_start: bool,
        algorithm: bool,
        use_fixed_numbers: bool = True,
    ) -> None:
        self.use_fixed_numbers = use_fixed_numbers
        if self.use_fixed_numbers:
            self.numbers = self.fixed_numbers.copy()
        else:
            self.numbers = self._generate_numbers(number_count)
        self.player_start = player_start
        self.computer = Computer(not self.player_start, self.numbers.copy(), level, algorithm)
        self.state = self.State.ACTIVE
        self.computer_score = 0
        self.computer_move = -1
        self.player_score = 0
        self.selection = 0
        self.turn = 0
        self.pending_ai_report = None
        self.result_logged = False
        self.ai_move_count = 0
        self.total_generated_vertices = 0
        self.total_evaluated_vertices = 0
        self.total_move_time = 0.0
        self._write_log_header(level)

    def reset(self) -> None:
        self.pending_ai_report = None
        self.result_logged = False
        self.ai_move_count = 0
        self.total_generated_vertices = 0
        self.total_evaluated_vertices = 0
        self.total_move_time = 0.0
        super().reset()

    def animate_move(self) -> None:
        if self.computer_move != -1:
            if self.selection == self.computer_move:
                self.select()
                self.computer_move = -1
                return

            if self.selection > self.computer_move:
                self.move_left()
            else:
                self.move_right()
        else:
            if self.turn % 2 == 0 and not self.player_start:
                self._queue_ai_move(self.computer_score, self.player_score)
            elif self.turn % 2 == 1 and self.player_start:
                self._queue_ai_move(self.player_score, self.computer_score)

    def select(self) -> None:
        player_turn = self._is_player_turn()
        ai_report = self.pending_ai_report

        super().select()

        if not player_turn:
            self.ai_move_count += 1

            if ai_report is None:
                generated_nodes = 0
                evaluated_nodes = 0
                elapsed_seconds = 0.0
            else:
                generated_nodes = int(ai_report["generated_nodes"])
                evaluated_nodes = int(ai_report["evaluated_nodes"])
                elapsed_seconds = float(ai_report["elapsed_seconds"])
            elapsed_ms = elapsed_seconds * 1000

            self.total_generated_vertices += generated_nodes
            self.total_evaluated_vertices += evaluated_nodes
            self.total_move_time += elapsed_seconds

            self._append_log(
                f"AI move {self.ai_move_count}: "
                f"generated vertices {generated_nodes}, "
                f"evaluated vertices {evaluated_nodes}, "
                f"time to figure out the move {elapsed_ms:.6f}ms"
            )
            self.pending_ai_report = None

        self._log_result()

    def _queue_ai_move(self, p1: int, p2: int) -> None:
        self.pending_ai_report = self.computer.action_with_metrics(
            self.numbers, p1, p2
        )
        self.computer_move = int(self.pending_ai_report["selection"])

    def _is_player_turn(self) -> bool:
        if self.turn % 2 == 0:
            return self.player_start

        return not self.player_start

    def _write_log_header(self, level: int) -> None:
        with self.log_path.open("w", encoding="utf-8") as log_file:
            if self.use_fixed_numbers:
                log_file.write("Numbers source: fixed\n")
            else:
                log_file.write("Numbers source: random\n")
            log_file.write(f"AI level: {level}\n")

    def _append_log(self, line: str) -> None:
        with self.log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(line + "\n")

    def _log_result(self) -> None:
        if self.result_logged or self.state != self.State.COMPLETE:
            return

        if self.player_score > self.computer_score:
            result = "Player"
        elif self.player_score < self.computer_score:
            result = "AI"
        else:
            result = "Draw"

        self._append_log(f"Winner: {result}")
        self._append_log(
            f"Total generated vertices: {self.total_generated_vertices}"
        )
        self._append_log(
            f"Total evaluated vertices: {self.total_evaluated_vertices}"
        )
        average_time = 0.0
        if self.ai_move_count > 0:
            average_time = self.total_move_time / self.ai_move_count
        self._append_log(f"Average time to move: {average_time * 1000:.6f}ms")
        self.result_logged = True
