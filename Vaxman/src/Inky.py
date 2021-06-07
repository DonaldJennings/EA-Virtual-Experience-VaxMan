from .Ghost import Ghost
from .Player import Player
class Inky(Ghost):

    _INKY_DIRECTIONS = [
    [30,0,2],
    [0,-15,4],
    [15,0,10],
    [0,15,7],
    [15,0,3],
    [0,-15,3],
    [15,0,3],
    [0,-15,15],
    [-15,0,15],
    [0,15,3],
    [15,0,15],
    [0,15,11],
    [-15,0,3],
    [0,-15,7],
    [-15,0,11],
    [0,15,3],
    [-15,0,11],
    [0,15,7],
    [-15,0,3],
    [0,-15,3],
    [-15,0,3],
    [0,-15,15],
    [15,0,15],
    [0,15,3],
    [-15,0,15],
    [0,15,11],
    [15,0,3],
    [0,-15,11],
    [15,0,11],
    [0,15,3],
    [15,0,1],
    ]

    

    _IL = len(_INKY_DIRECTIONS)-1
    _INKY_WIDTH = 303-16-32 #Inky width

    _TURNS = 0
    _STEPS = 0

    def reproduce(self):
          return Inky(self.rect.left, self.rect.top, "util/Inky.png")
        
    def changeSpeed(self):
      
      turn = self._TURNS
      steps = self._STEPS
      directions = self._INKY_DIRECTIONS
      l = self._IL
      try:
        z=directions[turn][2]
        if steps < z:
          self.change_x=directions[turn][0]
          self.change_y=directions[turn][1]
          steps+=1
        else:
          if turn < l:
            turn+=1
          else:
            turn = 0
          self.change_x=directions[turn][0]
          self.change_y=directions[turn][1]
          steps = 0
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
        return self._INKY_DIRECTIONS

    def getLength(self):
        return self._IL
    
    def getWidth(self):
        return self._INKY_WIDTH
    