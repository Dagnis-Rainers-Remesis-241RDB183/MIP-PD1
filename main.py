import asyncio

from pyray import *

from src.game import Game


async def main():
    game = Game()

    init_window(800, 450, "Hello")
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        draw_text(str(game.value), 190, 240, 20, RED)
        end_drawing()
        await asyncio.sleep(0)
    close_window()


if __name__ == "__main__":
    asyncio.run(main())
