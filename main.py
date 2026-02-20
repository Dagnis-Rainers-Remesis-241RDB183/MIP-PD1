import asyncio

from pyray import *


async def main():
    init_window(800, 450, "Hello")
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        end_drawing()
        await asyncio.sleep(0)
    close_window()


if __name__ == "__main__":
    asyncio.run(main())
