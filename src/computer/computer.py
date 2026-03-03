from ..node.node import Node  


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
        
        self.RootGameStateNode = None
    
    def SearchForOptimalActions(self,ProcessableNode:Node): 
        

        if (): # TODO: imlementēt modeļa 1) scenārija pārbaudi, kā arī child node parsošanu 
            self.UpdateNodeDistances()
        elif (len(ProcessableNode.ChildNodes==0)):
            ProcessableNode.ChildNodes = self.CreateNextNodes()
        if(ProcessableNode.ID>=len(ProcessableNode.ParentNode.ChildNodes-1)):
            self.SearchForOptimalActions(self,ProcessableNode.ParentNode)
        else:
            self.SearchForOptimalActions(self,ProcessableNode.ParentNode.ChildNodes[ProcessableNode.ID+1]) 
        
        
        

    def CheckIfEnd(self, CheckableNode:Node):
        pass


    def CreateNextNodes():
        NextNodes = []
        return NextNodes

    def UpdateNodeDistances(self,end_node:Node):
        
        CurrentNode = end_node
       
        while CurrentNode.ParentNode!=self.RootGameStateNode:
            if(CurrentNode.DistanceFromEnd+1<CurrentNode.ParentNode.DistanceFromEnd):
                CurrentNode.ParentNode.DistanceFromEnd=CurrentNode.DistanceFromEnd+1
                CurrentNode = CurrentNode.ParentNode
            else:
                break

    def Act(self):
        self.SearchForOptimalAction()




