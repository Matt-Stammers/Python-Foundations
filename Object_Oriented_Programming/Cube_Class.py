# simples:

class Cube:
    def __init__(self, side=0):
        self._side = side

    def get_side(self):
        return self._side
  
    def set_side(self, new_side):
        self._side = abs(new_side)
