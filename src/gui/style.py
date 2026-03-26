import config
from pyray import *
from typing import final


@final
class Style:
    def __init__(self) -> None:
        gui_load_style(str(config.THEME_STYLE_PATH))
        gui_set_style(0, 16, gui_get_font().baseSize * 2)

        gui_set_style(
            GuiControl.DEFAULT,
            GuiDefaultProperty.BACKGROUND_COLOR,
            gui_get_style(GuiControl.DEFAULT, GuiControlProperty.BASE_COLOR_PRESSED),
        )

        self.BACKGROUND_COLOR = get_color(
            gui_get_style(GuiControl.DEFAULT, GuiDefaultProperty.BACKGROUND_COLOR)
            & 0xFFFFFFFF
        )

        self.TEXT_COLOR_NORMAL = get_color(
            gui_get_style(GuiControl.DEFAULT, GuiControlProperty.TEXT_COLOR_NORMAL)
            & 0xFFFFFFFF
        )

        self.TEXT_COLOR_PRESSED = get_color(
            gui_get_style(GuiControl.DEFAULT, GuiControlProperty.TEXT_COLOR_PRESSED)
            & 0xFFFFFFFF
        )
