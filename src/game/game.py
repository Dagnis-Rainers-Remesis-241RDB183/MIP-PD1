import random
from enum import Enum


class Game:
    class State(Enum):
        START = 0
        ACTIVE = 1
        COMPLETE = 2

    computer_score: int
    numbers: list[int]
    player_score: int
    player_start: bool
    selection: int
    state: State
    turn: int

    def __init__(self) -> None:
        self.computer_score = 0
        self.numbers = []
        self.player_score = 0
        self.player_start = False
        self.selection = 0
        self.state = self.State.START
        self.turn = 0

    def move_left(self) -> None:
        self.selection = max(0, self.selection - 2)

    def move_right(self) -> None:
        self.selection = min(
            len(self.numbers) - 2 + len(self.numbers) % 2, self.selection + 2
        )

    def select(self) -> None:
        self.turn += 1
        a = self.numbers.pop(self.selection)

        if len(self.numbers) == self.selection:
            self._remove_point()

            self.selection = min(
                len(self.numbers) - 2 + len(self.numbers) % 2, self.selection
            )
            return

        b = self.numbers.pop(self.selection)
        self._replace(a, b)

        self.selection = min(
            len(self.numbers) - 2 + len(self.numbers) % 2, self.selection
        )

    def start(self, number_count: int, player_start: bool) -> None:
        self.computer_score = 0
        self.numbers = self._generate_numbers(number_count)
        self.player_score = 0
        self.player_start = player_start
        self.selection = 0
        self.state = self.State.ACTIVE
        self.turn = 0

    def _add_point(self) -> None:
        match self.turn % 2:
            case 0:
                if self.player_start:
                    self.computer_score += 1
                else:
                    self.player_score += 1
            case 1:
                if self.player_start:
                    self.player_score += 1
                else:
                    self.computer_score += 1
            case _:
                pass

    def _generate_numbers(self, count: int) -> list[int]:
        numbers: list[int] = []

        for _ in range(count):
            number = random.randint(1, 6)
            numbers.append(number)

        return numbers

    def _remove_point(self) -> None:
        match self.turn % 2:
            case 0:
                if self.player_start:
                    self.player_score -= 1
                else:
                    self.computer_score -= 1
            case 1:
                if self.player_start:
                    self.computer_score -= 1
                else:
                    self.player_score -= 1
            case _:
                pass

    def _replace(self, a: int, b: int) -> None:
        sum = a + b

        if sum > 6:
            self._add_point()
            sum -= 6

        self.numbers.insert(self.selection, sum)
