from ..game_state import GameState 

class Node:
    def __init__(self):
        self.GameState:GameState = None
        self.ChildNodes:list[Node] = []
        self.DistanceFromEnd = float('inf')