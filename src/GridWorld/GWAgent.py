from Agent import Agent
import numpy as np

class GridWorldAgent(Agent):
    def __init__(self, reward=0, state=None,policy= "random"):
        super().__init__(reward, state)
        self.policy =  policy
        self.name = "GridWorldAgent"
        
        
    def getAction(self, state):
        if self.policy == "random":
            action_x = np.random.randint(-1,1)
            action_y = np.random.randint(-1,1)
            action = [action_x,action_y]
        if self.policy == "humain":
            env_render = self.fromStateToRender(state)
            print(env_render)
            try :
                action = input("action : ")
                action = action.split(" ")
                action = [int(action[0]),int(action[1])]
            except:
                action = [0,0]
                
        if self.policy == "Qlearning":
            pass
        return action
    
    def fromStateToRender(self,state):
        from  GridWorld.GWEnvironnement import GWEnvironnement
        grid_shape = state[0]
        env = GWEnvironnement(grid_shape=grid_shape,entities=state[1:])
        return env.render()
        
    
    def update(self, state, reward):
        super().update(state, reward)
    
