from ..game_state import GameState 

class Node:
    def __init__(self):
        self.ParentNode:Node = None
        self.GameState = None
        self.ID = None
        self.ChildNodes = []
        self.DistanceFromEnd = float('inf')