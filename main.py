import asyncio

import py_hot_reload
from pyray import *

from src.game import Game
from src.gui import Gui

from src.computer import Computer


async def main() -> None:
    '''
    game = Game()
    gui = Gui(game)

    while not window_should_close():
        gui.render(game)
        await asyncio.sleep(0)
    close_window()
    '''  
    comp = Computer()
    comp.max_level=5
    comp.root_game_state_node.game_state.number_row = [1,3,6,4,5,1]
    comp.CreateTree(comp.root_game_state_node,0)
    comp.BuildJsonTree(comp.root_game_state_node,comp.tree,0)
    comp.PrintTree()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    py_hot_reload.run_with_reloader(run)
