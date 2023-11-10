from MarkovProperty import MarkovProperty

ActionSet = {
    "up" : [0, -1],
    "down" : [0, 1],
    "left" : [1, 0],
    "right" : [-1, 0],
    "stay" : [0, 0]
}
TranslateEntities = {
        "agent" : 0,
        "goal" : 1,
        "trap" : 2,
        "wall" : 3,
        "grill" : 4,
        "nothing" : 5
    }    

class GridWorldProperty(MarkovProperty):
    def __init__(self):
        super().__init__()
        self.S = self.initializeS()  # S : set of possible states
        self.A = self.initializeA()  # A : set of possible actions
        self.R = self.initializeR()  # R : distribution of reward given (state, action) pair
        self.P = self.initializeP()  # P : transition probability i.e. distribution over next state given (state, action) pair
        self.G = self.initializeG()  # G : discount factor

    def initializeS(self):
        # TODO: Implement this method
        pass

    def initializeA(self):
        # TODO: Implement this method
        pass

    def initializeR(self):
        # TODO: Implement this method
        pass

    def initializeP(self):
        # TODO: Implement this method
        pass

    def initializeG(self):
        # TODO: Implement this method
        pass