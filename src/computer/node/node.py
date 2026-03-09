from ..game_state import GameState 

class Node:
    def __init__(self):
        self.parent_node:Node = None
        self.game_state:GameState = None
        self.child_nodes:list[Node] = []
        self.distance_from_end = float('inf')