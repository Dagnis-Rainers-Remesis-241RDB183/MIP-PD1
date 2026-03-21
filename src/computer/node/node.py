from ..game_state import GameState 

class Node:
    def __init__(self):
        
        self.child_nodes:list[str] = []
        self.parent_node:str = ""