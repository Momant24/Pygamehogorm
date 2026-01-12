

BLOKK_STORELSE = 50

class Hogorm:
    def __init__(self):
        self.x, self.y, = BLOKK_STORELSE,  BLOKK_STORELSE
        self.xdir = 1   
        self.ydir = 0
        self.kropp = []