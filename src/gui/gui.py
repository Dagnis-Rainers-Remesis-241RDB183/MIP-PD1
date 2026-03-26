import sys
from typing import Any

from pyray import *

import config
from src.game import Game
from src.gui.style import Style


class Gui:
    number_count: Any
    player_start: Any
    level: Any
    algorithm: Any
    number_edit: bool
    level_edit: bool
    time: float
    animate_time: float
    selection_time: float
    selection_position: float
    style: Style

    def __init__(self, game: Game) -> None:
        if sys.platform == "darwin":
            set_config_flags(globals().get("FLAG_WINDOW_HIGHDPI", 0))

        init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, config.WINDOW_TITLE)
        set_target_fps(60)

        self.number_count = ffi.new("int *", 15)
        self.player_start = ffi.new("bool *", True)
        self.level = ffi.new("int *", 1)
        self.algorithm = ffi.new("bool *", True)
        self.number_edit = False
        self.level_edit = False
        self.time = 0.0
        self.animate_time = 0.0
        self.selection_time = 0.0
        self.selection_position = (
            config.WINDOW_WIDTH - len(game.numbers) * config.NUMBER_PADDING
        ) / 2
        self.style = Style()

    def render(self, game: Game) -> None:
        self.time += get_frame_time()

        begin_drawing()

        clear_background(self.style.BACKGROUND_COLOR)

        match game.state:
            case game.State.START:
                self._draw_start_screen(game)
            case game.State.ACTIVE:
                self._draw_active_screen(game)
            case game.State.COMPLETE:
                self._draw_complete_screen(game)

        end_drawing()

    def _draw_active_screen(self, game: Game) -> None:
        if self.time >= self.animate_time + 0.5:
            self.animate_time = self.time
            self.selection_time = self.time
            game.animate_move()

        length = len(game.numbers)

        window_offset = int((config.WINDOW_WIDTH - length * config.NUMBER_PADDING) / 2)
        selection_offset = game.selection * config.NUMBER_PADDING
        offset = window_offset + selection_offset

        self.selection_position = lerp(
            self.selection_position, offset, min(1, self.time - self.selection_time)
        )

        draw_rectangle_rec(
            Rectangle(self.selection_position - 10, 196, 80, 60),
            self.style.TEXT_COLOR_NORMAL,
        )

        draw_rectangle_lines_ex(
            Rectangle(self.selection_position - 10, 196, 80, 60),
            3.0,
            self.style.TEXT_COLOR_PRESSED,
        )

        offset = int((config.WINDOW_WIDTH - length * config.NUMBER_PADDING) / 2)

        for i in range(length):
            number = game.numbers[i]
            draw_text_ex(
                gui_get_font(),
                str(number),
                Vector2(offset + i * config.NUMBER_PADDING, 200),
                config.FONTSIZE,
                0,
                self.style.TEXT_COLOR_PRESSED,
            )

        _ = gui_label(Rectangle(200, 300, 200, 50), f"Player : {game.player_score}")
        _ = gui_label(Rectangle(800, 300, 200, 50), f"Computer : {game.computer_score}")

        if game.turn % 2 == 0 and not game.player_start:
            return
        elif game.turn % 2 == 1 and game.player_start:
            return

        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 160, 300, 50, 50), "#118#"):
            self.selection_time = self.time
            game.move_left()
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 + 110, 300, 50, 50), "#119#"):
            self.selection_time = self.time
            game.move_right()
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 100, 300, 200, 50), "Select"):
            game.select()

    def _draw_complete_screen(self, game: Game) -> None:
        if game.player_score > game.computer_score:
            draw_text_ex(
                gui_get_font(),
                "You win!",
                Vector2(config.WINDOW_WIDTH / 2 - 75, 200),
                config.FONTSIZE,
                0,
                self.style.TEXT_COLOR_PRESSED,
            )
        elif game.player_score == game.computer_score:
            draw_text_ex(
                gui_get_font(),
                "Draw.",
                Vector2(config.WINDOW_WIDTH / 2 - 75, 200),
                config.FONTSIZE,
                0,
                self.style.TEXT_COLOR_PRESSED,
            )
        else:
            draw_text_ex(
                gui_get_font(),
                "You lose :(",
                Vector2(config.WINDOW_WIDTH / 2 - 100, 200),
                config.FONTSIZE,
                0,
                self.style.TEXT_COLOR_PRESSED,
            )

        if gui_button(
            Rectangle(config.WINDOW_WIDTH / 2 - 200, 410, 400, 50), "Play again"
        ):
            game.reset()

    def _draw_start_screen(self, game: Game) -> None:
        draw_text_ex(
            gui_get_font(),
            "PD1 - Komanda 12",
            Vector2(390, 200),
            config.FONTSIZE,
            0,
            self.style.TEXT_COLOR_PRESSED,
        )

        if gui_spinner(
            Rectangle(config.WINDOW_WIDTH / 2 - 200, 270, 400, 50),
            "Numbers",
            self.number_count,
            15,
            25,
            self.number_edit,
        ):
            self.number_edit = not self.number_edit

        if gui_spinner(
            Rectangle(config.WINDOW_WIDTH / 2 - 200, 340, 400, 50),
            "Level",
            self.level,
            1,
            10,
            self.level_edit,
        ):
            self.level_edit = not self.level_edit

        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 200, 410, 400, 50), "Play"):
            game.start(
                int(self.number_count[0]),
                int(self.level[0]),
                bool(self.player_start[0]),
                bool(self.algorithm[0]),
            )

        _ = gui_check_box(
            Rectangle(config.WINDOW_WIDTH / 2 - 175, 480, 25, 25),
            "Start first",
            self.player_start,
        )

        _ = gui_check_box(
            Rectangle(config.WINDOW_WIDTH / 2 + 25, 480, 25, 25),
            "Alfa-beta" if bool(self.algorithm[0]) else "Min-max",
            self.algorithm,
        )
