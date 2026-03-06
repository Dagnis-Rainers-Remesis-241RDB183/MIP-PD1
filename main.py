import asyncio

import py_hot_reload
from pyray import *

from src.game import Game
from src.gui import Gui


async def main() -> None:
    game = Game()
    gui = Gui(game)

    while not window_should_close():
        gui.render(game)
        await asyncio.sleep(0)
    close_window()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    py_hot_reload.run_with_reloader(run)
