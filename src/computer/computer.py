from .node import Node  
from .game_state import GameState
import json

class Computer:
    
    def __init__(self,RootKey:str="0|123456|0"):
        
        self.root_game_state_node_key:str = RootKey
        self.computer_P1:bool = True
        self.max_level:int = 0
        self.tree:dict[str,Node] = {}
        self.json_tree:dict = {}

    #Uzlabota CreatTree loģika
    def CreateTree(self,ProcessableNodeKey:str,Level:int): 
        if Level > self.max_level:
            return
        if(ProcessableNodeKey not in self.tree):
            self.tree[ProcessableNodeKey] = Node()
        if(len(self.tree[ProcessableNodeKey].child_nodes)==0):
            self.tree[ProcessableNodeKey]=self.CreateNextNodes(ProcessableNodeKey)
        for i in range(len(self.tree[ProcessableNodeKey].child_nodes)):
            self.CreateTree(self.tree[ProcessableNodeKey].child_nodes[i],Level+1)
                    
    def GetBestAction(self,NextNodes:list[Node]): # implementēt heiristisku analīzi, atšķirt datora un pretinieka gājienus
        # Izvērtē cik tālu ir end, cik liela ir punktu atšķirība pēc gājiena
        # 0 - 0 | 1- 0 0-1 0-0 , 
        id
        return id   
        

    def CheckIfEnd(self, CheckableKey):
        current_P1,current_row, current_P2 = self.extractFromGameState(CheckableKey)
        if(len(current_row)==1):
            if(self.computer_P1==True and current_P1>current_P2):
                return True   
            elif(self.computer_P1==False and current_P1<current_P2):
                return True
            

    def extractFromGameState(self,Key:str):
       

        splitkey = Key.split('|')
        return int(splitkey[0]),splitkey[1],int(splitkey[2])
    
    def CreateNextNodes(self,ParentNodeKey:str): # Izveidot nākamos game states
        NextStates:Node = Node()
        current_P1,current_row, current_P2 = self.extractFromGameState(ParentNodeKey)
        
        current_distance= len(current_row)
        if(current_distance==1):
            return NextStates
        
        p1,rootRow,p2 = self.extractFromGameState(self.root_game_state_node_key)
        root_distance = len(rootRow)
        turns_played = root_distance - current_distance
        P1_turn = (turns_played % 2 == 0)

        for i in range(0, current_distance-1, 2):
            a = int(current_row[i])
            b = int(current_row[i+1])
            sum = a + b

            add_points = 0
            if sum > 6:
                add_points = 1
                sum -= 6

            next_row = current_row[:i] + str(sum) + current_row[i+2:]
            if P1_turn:
                current_P1 += add_points
            else:
                current_P2 += add_points
            new_state = GameState(next_row, current_P1, current_P2)
            
            NextStates.child_nodes.append(new_state.state)
            self.tree[new_state.state]=Node()

        if current_distance % 2 != 0:
            new_row = current_row[:-1]

            

            if P1_turn:
                current_P2 -= 1
            else:                
                current_P1 -= 1
            new_state = GameState(new_row, current_P1, current_P2)

          
            NextStates.child_nodes.append(new_state.state)
            self.tree[new_state.state]=Node()

        NextStates.parent_node=ParentNodeKey
        return NextStates
    
    def PrintTree(self):
        self.BuildJsonTree(self.root_game_state_node_key,self.json_tree)

        jt =  json.dumps(self.json_tree,indent=4)

        with open("tree.json","w") as f:
            f.write(jt)

    def BuildJsonTree(self,ParentKey:str,UpperDict:dict):
        
        for key in self.tree[ParentKey].child_nodes:
            UpperDict[key]={}
            self.BuildJsonTree(key,UpperDict[key])

    def UpdateNodeDistances(self,end_node:Node): # Iespējams jāsavieno ar GetBestGameStateNode
        pass
        """
        CurrentNode = end_node
       
        while CurrentNode.parent_node!=self.root_game_state_node:
            if(CurrentNode.distance_from_end+1<CurrentNode.parent_node.distance_from_end):
                CurrentNode.parent_node.distance_from_end=CurrentNode.distance_from_end+1
                CurrentNode = CurrentNode.parent_node
            else:
                break
        """
        

    def Act(self,maxLevel:int):
       
        self.CreateTree(self.root_game_state_node,self.root_game_state_node.level+maxLevel)
        self.GetBestAction(self.root_game_state_node.child_nodes)



