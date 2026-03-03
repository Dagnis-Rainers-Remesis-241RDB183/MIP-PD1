from game_state.game_state import GameState

class Computer:
    
    def __init__(self):
        """
            sobrideja teorija:
            visticamak jaizveido metode, kas nems sobridejo gamestate un mekles lidz noteiktam limenim optimalako next gamestate,
            mainot sobridejo game state ar iespejamiem gajieniem 
        """
        self.CurrentGameState = None
        self.Level = 0
        self.Action = None
        
    def GetPossibleActions(self) ->GameState: # returns list of actions
        return self.CurrentGameState
    
    def SearchForOptimalAction(self): # recursively 
        if (len(self.CurrentGameState.Skaitlu_virkne)%2==0):
            c = self.GetPossibleActions()
            print(c.Skaitlu_virkne)

    def Act(self):
        self.searchForOptimalAction()



""""
{
    a1: 2
    a2: 4


}

a1
b1 b2




"""