from .Ghost import Ghost

class Pinky(Ghost):
    _PinkyDirections = [
        [0,-30,4],
        [15,0,9],
        [0,15,11],
        [-15,0,23],
        [0,15,7],
        [15,0,3],
        [0,-15,3],
        [15,0,19],
        [0,15,3],
        [15,0,3],
        [0,15,3],
        [15,0,3],
        [0,-15,15],
        [-15,0,7],
        [0,15,3],
        [-15,0,19],
        [0,-15,11],
        [15,0,9]
    ]

    _pl = len(_PinkyDirections)-1
    _steps = 0
    _turns = 0

    def reproduce(self):
        return Pinky(self.rect.left, self.rect.top, "util/Pinky.png")

    def changeSpeed(self):
        steps = int(self._steps)
        turn = int(self._turns)
        directions = self._PinkyDirections

        try:
            z=directions[turn][2]
            if steps < z:
                self.change_x=directions[turn][0]
                self.change_y=directions[turn][1]
                steps+=1
            else:
                if turn < self._pl:
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
        return self._PinkyDirections

    def getLength(self):
        return self._pl
    
    def getWidth(self):
        return 303-16
    