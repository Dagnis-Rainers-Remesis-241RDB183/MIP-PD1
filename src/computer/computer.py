from .node import Node  
from .game_state import GameState
import json

class Computer:
    
    def __init__(self):
        
        self.root_game_state_node:Node = Node()
        self.computer_P1:bool = True
        self.max_level:int = 0
        self.tree:dict = {}

    #Uzlabota CreatTree loģika
    def CreateTree(self,ProcessableNode:Node,Level:int): 
        if Level > self.max_level or self.CheckIfEnd(ProcessableNode):
            return
        if(len(ProcessableNode.child_nodes)==0):
                ProcessableNode.child_nodes=self.CreateNextNodes(ProcessableNode)
        for i in range(len(ProcessableNode.child_nodes)):
            ChildNode:Node = ProcessableNode.child_nodes[i]
            if(self.CheckIfEnd(ChildNode)):
                self.UpdateNodeDistances(ProcessableNode)
            
            self.CreateTree(ChildNode,Level+1)
                    
    def GetBestAction(self,NextNodes:list[Node]): # implementēt heiristisku analīzi, atšķirt datora un pretinieka gājienus
        # Izvērtē cik tālu ir end, cik liela ir punktu atšķirība pēc gājiena
        # 0 - 0 | 1- 0 0-1 0-0 , 
        id
        return id   
        

    def CheckIfEnd(self, CheckableNode:Node):
        if(len(CheckableNode.game_state.number_row)==1):
            if(self.computer_P1==True and CheckableNode.game_state.P1>CheckableNode.game_state.P2):
                return True   
            elif(self.computer_P1==False and CheckableNode.game_state.P1<CheckableNode.game_state.P2):
                return True
            

    def CreateNextNodes(self,ParentNode:Node): # Izveidot nākamos game state nodes
        NextNodes:list[Node] = []
        
        current_state = ParentNode.game_state
        current_row = current_state.number_row
        current_distance= len(current_row)

        root_distance = len(self.root_game_state_node.game_state.number_row)
        turns_played = root_distance - current_distance
        P1_turn = (turns_played % 2 == 0)

        for i in range(0, current_distance-1, 2):
            a = current_row[i]
            b = current_row[i+1]
            sum = a + b

            add_points = 0
            if sum > 6:
                add_points = 1
                sum -= 6

            next_row = current_row[:i] + [sum] + current_row[i+2:]

            new_state = GameState(next_row, current_state.P1, current_state.P2)

            if P1_turn:
                new_state.P1 += add_points
            else:
                new_state.P2 += add_points

            new_node = Node()
            new_node.game_state = new_state
            NextNodes.append(new_node)

        if current_distance % 2 != 0:
            new_node = current_row[:-1]

            new_state = GameState(new_node, current_state.P1, current_state.P2)

            if P1_turn:
                new_state.P2 -= 1
            else:                
                new_state.P1 -= 1
        
            new_node = Node()
            new_node.game_state = new_state
            NextNodes.append(new_node)

        for cn in NextNodes:
            cn.parent_node = ParentNode
        return NextNodes
    
    def PrintTree(self):
        json_tree =  json.dumps(self.tree,indent=4)
    
        with open("tree.json","w") as f:
            f.write(json_tree)

    def BuildJsonTree(self,ParentNode:Node,ParentDict:dict,level:int):
        if (level>=self.max_level):
            return
        for i in range(len(ParentNode.child_nodes)):
            SaveableNode:Node = ParentNode.child_nodes[i]
            SaveableGameState:str = ""
            if (self.computer_P1):
                SaveableGameState+=str(SaveableNode.game_state.P1)+"_"
                for num in SaveableNode.game_state.number_row:
                    SaveableGameState+=str(num)
                SaveableGameState+="_"+str(SaveableNode.game_state.P2)
            else:
                SaveableGameState+=str(SaveableNode.game_state.P2)+"_"
                for num in SaveableNode.game_state.number_row:
                    SaveableGameState+=str(num)
                SaveableGameState+="_"+str(SaveableNode.game_state.P1)
            ParentDict[SaveableGameState] = {}
            self.BuildJsonTree(SaveableNode,ParentDict[SaveableGameState],level+1)

    def UpdateNodeDistances(self,end_node:Node): # Iespējams jāsavieno ar GetBestGameStateNode
        
        CurrentNode = end_node
       
        while CurrentNode.parent_node!=self.root_game_state_node:
            if(CurrentNode.distance_from_end+1<CurrentNode.parent_node.distance_from_end):
                CurrentNode.parent_node.distance_from_end=CurrentNode.distance_from_end+1
                CurrentNode = CurrentNode.parent_node
            else:
                break

    def Act(self,maxLevel:int):
        self.CreateTree(self.root_game_state_node,self.root_game_state_node.level+maxLevel)
        self.GetBestAction(self.root_game_state_node.child_nodes)



