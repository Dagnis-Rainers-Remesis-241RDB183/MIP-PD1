import asyncio

import py_hot_reload
from pyray import *

import config
from src.game import Game


def init() -> None:
    init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, "MIP-PD1")
    gui_load_style("assets/theme/style_bluish.rgs")
    gui_set_style(0, 16, gui_get_font().baseSize * 2)
    set_target_fps(60)


def draw_numbers(game: Game) -> None:
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


def draw_controls(game: Game) -> None:
    if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 160, 300, 50, 50), "#118#"):
        game.move_left()
    if gui_button(Rectangle(config.WINDOW_WIDTH / 2 + 110, 300, 50, 50), "#119#"):
        game.move_right()
    if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 100, 300, 200, 50), "Select"):
        game.select()


def draw_selection(game: Game) -> None:
    length = len(game.numbers)
    windowOffset = int((config.WINDOW_WIDTH - length * config.NUMBER_PADDING) / 2)
    selectionOffset = game.selection * config.NUMBER_PADDING
    offset = windowOffset + selectionOffset

    draw_rectangle_rounded(
        Rectangle(offset - 10, 196, 80, 60), 0.1, 1, get_color(gui_get_style(0, 20))
    )
    draw_rectangle_rounded_lines_ex(
        Rectangle(offset - 10, 196, 80, 60), 0.3, 1, 4.0, get_color(gui_get_style(0, 2))
    )


def draw_scores(game: Game) -> None:
    _ = gui_label(Rectangle(200, 300, 200, 50), f"Player : {game.playerScore}")
    _ = gui_label(Rectangle(800, 300, 200, 50), f"Computer : {game.computerScore}")


def render(game: Game) -> None:
    begin_drawing()

    clear_background(WHITE)
    draw_fps(get_render_width() - 90, 10)

    draw_numbers(game)
    draw_controls(game)
    draw_selection(game)
    draw_scores(game)

    end_drawing()


async def main() -> None:
    game = Game()

    init()

    while not window_should_close():
        render(game)
        await asyncio.sleep(0)
    close_window()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    py_hot_reload.run_with_reloader(run)
