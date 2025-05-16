class Position:
    def __init__(self, x,y,value,terminalstate):
        self.x = x
        self.y = y
        self.value = value
        self.terminalstate = terminalstate

    def __repr__(self):
        return f"Position({self.x}, {self.y},{self.value},{self.terminalstate})"