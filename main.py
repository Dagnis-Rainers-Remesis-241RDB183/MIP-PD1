from pyray import *

from src.game import Game
from src.gui import Gui


def main() -> None:
    game = Game()
    gui = Gui(game)

    while not window_should_close():
        gui.render(game)
    close_window()


if __name__ == "__main__":
    main()
