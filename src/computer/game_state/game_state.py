class GameState:
    def __init__(self,NumberRow=[],p1:int=0,p2:int=0):
        
        self.state:str = str(p1)+"|"
        for num in NumberRow:
            self.state+=str(num)
        self.state += "|"+str(p2)
        
        

    