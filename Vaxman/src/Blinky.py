
import pygame
from .Ghost import Ghost

class Blinky(Ghost):

    _BLINKY_DIRECTIONS = [
            [0,-15,4],
            [15,0,9],
            [0,15,11],
            [15,0,3],
            [0,15,7],
            [-15,0,11],
            [0,15,3],
            [15,0,15],
            [0,-15,15],
            [15,0,3],
            [0,-15,11],
            [-15,0,3],
            [0,-15,11],
            [-15,0,3],
            [0,-15,3],
            [-15,0,7],
            [0,-15,3],
            [15,0,15],
            [0,15,15],
            [-15,0,3],
            [0,15,3],
            [-15,0,3],
            [0,-15,7],
            [-15,0,3],
            [0,15,7],
            [-15,0,11],
            [0,-15,7],
            [15,0,5]
        ]

    _BL = len(_BLINKY_DIRECTIONS)-1
    _steps = 0
    _turns = 0

    def reproduce(self):
        return Blinky(self.rect.left, self.rect.top, "util/Blinky.png")
        
    def changeSpeed(self):
        steps = int(self._steps)
        turn = int(self._turns)
        directions = self._BLINKY_DIRECTIONS

        try:
            z=directions[turn][2]
            if steps < z:
                self.change_x=directions[turn][0]
                self.change_y=directions[turn][1]
                steps+=1
            else:
                if turn < self._BL:
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
        return self._turns
    
    def getSteps(self):
        return self._steps

    def setTurns(self, turns):
        self._turns = turns
    
    def setSteps(self, steps):
        self._steps = steps

    def getDirections(self):
        return self._BLINKY_DIRECTIONS

    def getLength(self):
        return self._BL
    
    def getHeight(self):
        return (3*60)+19
    