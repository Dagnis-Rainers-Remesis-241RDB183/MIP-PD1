from .node import Node  


"""
    šobrīdējais teorētiskais modelis:
    Veido nodes ar no sobrideja gamestate lidz noteiktam limenim, vai ari pasa sakuma gamestate.
    Ja node izveide konstatē ka ir:
    1) End game, izsauc UpdateNodeDistance un SearchForOptimalActions parso sibling node
    2) Last sibling, izsauc SearchForOptimalActions parso parent node
    3) Strupceļa node, izsauc SearchForOptimalActions parso sibling node

    


"""

class Computer:
    
    def __init__(self):
        
        self.RootGameStateNode:Node = None
        self.ComputerP1:bool = True




    def CreateTree(self,ProcessableNode:Node,maxLevel:int): 
        
        if (self.CheckIfEnd()):
            self.UpdateNodeDistances()
        if(len(ProcessableNode.ChildNodes)==0):
            ProcessableNode.ChildNodes = self.CreateNextNodes() # TODO: implementēt child nodes
        if(ProcessableNode.Level<maxLevel):
            for i in range(len(ProcessableNode.ChildNodes)):
                if(ProcessableNode.ChildNodes[i].Checked==False):
                    ProcessableNode.ChildNodes[i].Checked==True
                    self.CreateTree(ProcessableNode.ChildNodes[i])
                    return
        if(ProcessableNode.ID>=len(ProcessableNode.ParentNode.ChildNodes-1)):
            self.CreateTree(self,ProcessableNode.ParentNode)
            return
        elif(ProcessableNode.Level<maxLevel and ProcessableNode.Level < maxLevel):
            self.CreateTree(self,ProcessableNode.ParentNode.ChildNodes[ProcessableNode.ID+1]) 
            return
        
            
                    
                
 

    def GetBestAction(NextNodes:list[Node]): # implementēt heiristisku analīzi, atšķirt datora un pretinieka gājienus
        # Izvērtē cik tālu ir end, cik liela ir punktu atšķirība pēc gājiena

        id
        return id   
        

    def CheckIfEnd(self, CheckableNode:Node):
        if(len(CheckableNode.GameState.NumberRow)==1):
            if(self.ComputerP1==True and CheckableNode.GameState.P1>CheckableNode.GameState.P2):
                return True   
            elif(self.ComputerP1==False and CheckableNode.GameState.P1<CheckableNode.GameState.P2):
                return True
            

    def CreateNextNodes(): # Izveidot nākamos game state nodes
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
        self.SearchForEnds(self.RootGameStateNode,self.RootGameStateNode.level+maxLevel)
        self.GetBestAction()



