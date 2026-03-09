from .node import Node  


class Computer:
    
    def __init__(self):
        
        self.RootGameStateNode:Node = None
        self.ComputerP1:bool = True
        self.MaxLevel:int = 0



    def CreateTree(self,ProcessableNode:Node,Level:int): 
        if (len(ProcessableNode.ChildNodes)==0 or Level > self.MaxLevel):
            return
        for i in range(len(ProcessableNode.ChildNodes)):
            ChildNode:Node = ProcessableNode.ChildNodes[i]
            if(self.CheckIfEnd(ChildNode)):
                self.UpdateNodeDistances(ProcessableNode)
            if(len(ChildNode.ChildNodes)==0):
                ChildNode.ChildNodes=self.CreateNextNodes(ChildNode)
            self.CreateTree(ChildNode,Level+1)

                    
    def GetBestAction(self,NextNodes:list[Node]): # implementēt heiristisku analīzi, atšķirt datora un pretinieka gājienus
        # Izvērtē cik tālu ir end, cik liela ir punktu atšķirība pēc gājiena
        # 0 - 0 | 1- 0 0-1 0-0 , 
        id
        return id   
        

    def CheckIfEnd(self, CheckableNode:Node):
        if(len(CheckableNode.GameState.NumberRow)==1):
            if(self.ComputerP1==True and CheckableNode.GameState.P1>CheckableNode.GameState.P2):
                return True   
            elif(self.ComputerP1==False and CheckableNode.GameState.P1<CheckableNode.GameState.P2):
                return True
            

    def CreateNextNodes(self): # Izveidot nākamos game state nodes
        NextNodes = []
        return NextNodes

    def UpdateNodeDistances(self,end_node:Node): # Iespējams jāsavieno ar GetBestGameStateNode
        
        CurrentNode = end_node
       
        while CurrentNode.ParentNode!=self.RootGameStateNode:
            if(CurrentNode.DistanceFromEnd+1<CurrentNode.ParentNode.DistanceFromEnd):
                CurrentNode.ParentNode.DistanceFromEnd=CurrentNode.DistanceFromEnd+1
                CurrentNode = CurrentNode.ParentNode
            else:
                break

    def Act(self,maxLevel:int):
        self.CreateTree(self.RootGameStateNode,self.RootGameStateNode.level+maxLevel)
        self.GetBestAction(self.RootGameStateNode.ChildNodes)



