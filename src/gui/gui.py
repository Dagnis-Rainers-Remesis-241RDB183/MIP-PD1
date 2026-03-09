import _cffi_backend
from pyray import *

import config
from src.game import Game
from src.gui.style import Style


class Gui:
    number_count: _cffi_backend.FFI.CData
    number_edit: bool
    player_start: _cffi_backend.FFI.CData
    time: float
    selection_time: float
    selection_position: float
    style: Style

    def __init__(self, game: Game) -> None:
        init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, "MIP-PD1")
        set_target_fps(60)

        self.number_count = ffi.new("int *", 15)
        self.number_edit = False
        self.player_start = ffi.new("bool *", True)
        self.time = 0.0
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
        length = len(game.numbers)

        # draw_selection
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

        # draw_numbers
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

        # draw_scores
        _ = gui_label(Rectangle(200, 300, 200, 50), f"Player : {game.player_score}")
        _ = gui_label(Rectangle(800, 300, 200, 50), f"Computer : {game.computer_score}")

        # draw_controls
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 160, 300, 50, 50), "#118#"):
            self.selection_time = self.time
            game.move_left()
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 + 110, 300, 50, 50), "#119#"):
            self.selection_time = self.time
            game.move_right()
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 100, 300, 200, 50), "Select"):
            game.select()

    def _draw_complete_screen(self, game: Game) -> None:
        pass

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
            "",
            self.number_count,
            15,
            25,
            self.number_edit,
        ):
            self.number_edit = not self.number_edit

        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 200, 340, 400, 50), "Play"):
            game.start(int(self.number_count[0]), bool(self.player_start[0]))

        _ = gui_check_box(
            Rectangle(config.WINDOW_WIDTH / 2 - 200, 410, 25, 25),
            "Start first",
            self.player_start,
        )
