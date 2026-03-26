from pyray import *

import config
from src.game.experiment_game import ExperimentGame

from .gui import Gui


class ExperimentGui(Gui):
    def __init__(self, game: ExperimentGame) -> None:
        super().__init__(game)
        self.use_fixed_numbers = ffi.new("bool *", True)

    def _draw_start_screen(self, game: ExperimentGame) -> None:
        draw_text_ex(
            gui_get_font(),
            "PD1 - Komanda 12",
            Vector2(390, 170),
            config.FONTSIZE,
            0,
            self.style.TEXT_COLOR_PRESSED,
        )

        _ = gui_check_box(
            Rectangle(config.WINDOW_WIDTH / 2 - 175, 250, 25, 25),
            "Use set numbers",
            self.use_fixed_numbers,
        )

        if bool(self.use_fixed_numbers[0]):
            _ = gui_label(
                Rectangle(config.WINDOW_WIDTH / 2 - 200, 290, 400, 50),
                "Set numbers: 614646222333533",
            )
        else:
            if gui_spinner(
                Rectangle(config.WINDOW_WIDTH / 2 - 200, 290, 400, 50),
                "Numbers",
                self.number_count,
                15,
                25,
                self.number_edit,
            ):
                self.number_edit = not self.number_edit

        if gui_spinner(
            Rectangle(config.WINDOW_WIDTH / 2 - 200, 360, 400, 50),
            "Level",
            self.level,
            1,
            10,
            self.level_edit,
        ):
            self.level_edit = not self.level_edit

        if gui_button(Rectangle(config.WINDOW_WIDTH / 2 - 200, 430, 400, 50), "Play"):
            game.start(
                int(self.number_count[0]),
                int(self.level[0]),
                bool(self.player_start[0]),
                bool(self.algorithm[0]),
                bool(self.use_fixed_numbers[0]),
            )

        _ = gui_check_box(
            Rectangle(config.WINDOW_WIDTH / 2 - 175, 500, 25, 25),
            "Start first",
            self.player_start,
        )

        _ = gui_check_box(
            Rectangle(config.WINDOW_WIDTH / 2 + 25, 500, 25, 25),
            "Alfa-beta" if bool(self.algorithm[0]) else "Min-max",
            self.algorithm,
        )

        _ = gui_label(
            Rectangle(config.WINDOW_WIDTH / 2 - 200, 550, 400, 30),
            "Experiment metrics are written to test_logs.txt",
        )
