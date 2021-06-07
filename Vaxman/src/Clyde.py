from .Ghost import Ghost
from .Player import Player
class Clyde(Ghost):

    _CLYDE_DIRECTIONS = [
[-30,0,2],
[0,-15,4],
[15,0,5],
[0,15,7],
[-15,0,11],
[0,-15,7],
[-15,0,3],
[0,15,7],
[-15,0,7],
[0,15,15],
[15,0,15],
[0,-15,3],
[-15,0,11],
[0,-15,7],
[15,0,3],
[0,-15,11],
[15,0,9],
]

    

    _CL = len(_CLYDE_DIRECTIONS)-1
    _CLYDE_WIDTH = 303+(32-16) #Inky width

    _TURNS = 0
    _STEPS = 0

        
    def changeSpeed(self):
      
      turn = self._TURNS
      steps = self._STEPS
      directions = self._CLYDE_DIRECTIONS
      l = self._CL
      try:
        z=directions[turn][2]
        if steps < z:
          self.change_x=directions[turn][0]
          self.change_y=directions[turn][1]
          steps+=1
        else:
            if turn < 1:
                turn += 1
            else:
                turn = 2
        return [turn,steps]
      except IndexError:
         return [0,0]

    def getTurns(self):
        return self._TURNS
    
    def getSteps(self):
        return self._STEPS

    def setTurns(self, turns):
        self._TURNS = turns
    
    def setSteps(self, steps):
        self._STEPS = steps

    def getDirections(self):
        return self._CLYDE_DIRECTIONS

    def getLength(self):
        return self._CL
    
    def getWidth(self):
        return self._CLYDE_WIDTH
    