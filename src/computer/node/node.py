from ..game_state import GameState 

class Node:
    def __init__(self):
        self.ParentNode:Node = None
        self.GameState:GameState = None
        self.ID:int = None
        self.ChildNodes:list[Node] = []
        self.DistanceFromEnd = float('inf')
        self.Checked:bool = False