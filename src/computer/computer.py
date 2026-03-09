from .node import Node  


class Computer:
    
    def __init__(self):
        
        self.root_game_state_node:Node = None
        self.computer_P1:bool = True
        self.max_level:int = 0



    def CreateTree(self,ProcessableNode:Node,Level:int): 
        if (len(ProcessableNode.child_nodes)==0 or Level > self.max_level):
            return
        for i in range(len(ProcessableNode.child_nodes)):
            ChildNode:Node = ProcessableNode.child_nodes[i]
            if(self.CheckIfEnd(ChildNode)):
                self.UpdateNodeDistances(ProcessableNode)
            if(len(ChildNode.child_nodes)==0):
                ChildNode.child_nodes=self.CreateNextNodes(ChildNode)
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
        for cn in NextNodes:
            cn.parent_node = ParentNode
        return NextNodes

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



