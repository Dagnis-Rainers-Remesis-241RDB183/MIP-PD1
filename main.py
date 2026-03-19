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
    comp = Computer("0|1234512345|0")
    comp.max_level=10
    comp.CreateTree(comp.root_game_state_node_key,0)
    comp.PrintTree()
    print(comp.tree[comp.root_game_state_node_key].child_nodes)

def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    py_hot_reload.run_with_reloader(run)
