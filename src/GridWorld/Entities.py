from abc import ABC, abstractmethod

class Entities(ABC):
    Types = ["agent","trap","wall","goal"]
    @abstractmethod
    def __init__(self,type,position,reward):
        self.type = type
        self.position = position
        self.reward = None
    def __str__(self):
        return self.type
    
class Agent(Entities):
    def __init__(self,position, reward=0):
        super().__init__("agent",position, reward)
class Trap(Entities):
    def __init__(self,position, reward=-1):
        super().__init__("trap",position, reward)
class Wall(Entities):
    def __init__(self,position, reward=-10):
        super().__init__("wall",position, reward)
class Goal(Entities):
    def __init__(self,position, reward=100):
        super().__init__("goal",position, reward)
        
        
EntitiesList = [Agent,Trap,Wall,Goal]