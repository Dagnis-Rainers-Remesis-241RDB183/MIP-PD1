import py_hot_reload
from pyray import *

from src.game import Game
from src.computer import Computer
from src.computer.game_state import GameState
from src.computer.node import Node
def main():
    game = Game()

    n1 = Node()
    print(n1.DistanceFromEnd)

    gs = GameState("12345")
    print(gs.NumberRow)

    c = Computer()
    c.RootGameStateNode=gs
    print(c.RootGameStateNode)

    init_window(800, 450, "Hello")
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        draw_text(str(game.value), 190, 240, 20, RED)
        end_drawing()
    close_window()
   
    

if __name__ == "__main__":
    py_hot_reload.run_with_reloader(main)
