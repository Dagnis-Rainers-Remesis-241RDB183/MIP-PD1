from pyray import *

from src.game.experiment_game import ExperimentGame
from src.gui.experiment_gui import ExperimentGui


def main() -> None:
    game = ExperimentGame()
    gui = ExperimentGui(game)

    while not window_should_close():
        gui.render(game)
    close_window()


if __name__ == "__main__":
    main()
