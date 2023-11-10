from Agent import Agent
import numpy as np

class GridWorldAgent(Agent):
    def __init__(self, reward=0, state=None,policy= "random"):
        super().__init__(reward, state)
        self.policy =  policy
        
        
    def getAction(self, state):
        if self.policy == "random":
            action_x = np.random.randint(-1,1)
            action_y = np.random.randint(-1,1)
            action = [action_x,action_y]
        return action
    
    def update(self, state, reward):
        super().update(state, reward)
    
