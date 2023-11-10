from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self,reward=None,state=None):
        # Todo: initialize the variables you will need
        self.reward = reward
        self.state = state

    @abstractmethod
    def getAction(self, state):
        # Todo: return the action to take
        pass

    @abstractmethod
    def update(self, state, reward):
        self.reward = reward
        self.state = state