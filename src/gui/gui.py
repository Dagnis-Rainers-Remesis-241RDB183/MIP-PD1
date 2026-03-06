from pyray import *

import config
from src.game import Game


class Gui:
    time: float
    selectionTime: float
    selectionPosition: float

    def __init__(self, game: Game) -> None:
        init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, "MIP-PD1")
        gui_load_style("assets/theme/style_bluish.rgs")
        gui_set_style(0, 16, gui_get_font().baseSize * 2)
        set_target_fps(60)

        self.time = 0.0
        self.selectionTime = 0.0
        self.selectionPosition = (
            config.WINDOW_WIDTH - len(game.numbers) * config.NUMBER_PADDING
        ) / 2

    def render(self, game: Game) -> None:
        self.time += get_frame_time()

        begin_drawing()

        clear_background(WHITE)
        draw_fps(get_render_width() - 90, 10)

        self._draw_numbers(game)
        self._draw_controls(game)
        self._draw_selection(game)
        self._draw_scores(game)

        end_drawing()

    def _draw_numbers(self, game: Game) -> None:
        length = len(game.numbers)
        offset = int((config.WINDOW_WIDTH - length * config.NUMBER_PADDING) / 2)

        for i in range(length):
            number = game.numbers[i]
            draw_text_ex(
                gui_get_font(),
                str(number),
                Vector2(offset + i * config.NUMBER_PADDING, 200),
                config.FONTSIZE,
                0,
                get_color(gui_get_style(0, 0)),
            )

    def _draw_controls(self, game: Game) -> None:
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 160, 300, 50, 50), "#118#"):
            self.selectionTime = self.time
            game.move_left()
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 + 110, 300, 50, 50), "#119#"):
            self.selectionTime = self.time
            game.move_right()
        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 100, 300, 200, 50), "Select"):
            game.select()

    def _draw_selection(self, game: Game) -> None:
        length = len(game.numbers)
        windowOffset = int((config.WINDOW_WIDTH - length * config.NUMBER_PADDING) / 2)
        selectionOffset = game.selection * config.NUMBER_PADDING
        offset = windowOffset + selectionOffset

        self.selectionPosition = lerp(
            self.selectionPosition, offset, min(1, self.time - self.selectionTime)
        )

        draw_rectangle_rounded(
            Rectangle(self.selectionPosition - 10, 196, 80, 60),
            0.1,
            1,
            get_color(gui_get_style(0, 20)),
        )
        draw_rectangle_rounded_lines_ex(
            Rectangle(self.selectionPosition - 10, 196, 80, 60),
            0.3,
            1,
            4.0,
            get_color(gui_get_style(0, 2)),
        )

    def _draw_scores(self, game: Game) -> None:
        _ = gui_label(Rectangle(200, 300, 200, 50), f"Player : {game.playerScore}")
        _ = gui_label(Rectangle(800, 300, 200, 50), f"Computer : {game.computerScore}")
