from Agent import Agent
import numpy as np
from GWQlearning import GWDeepQlearning

class GridWorldAgent(Agent):
    def __init__(self,grid_size,num_entities, reward=0, state=None,policy= "random"):
        super().__init__(reward, state)
        self.policy =  policy
        self.name = "GridWorldAgent"
        self.GWDeepQlearning = GWDeepQlearning(grid_size, num_entities)
        
        
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
                print("action non valide. format attendu : x y")
                
        if self.policy == "Qlearning":
            action = self.GWDeepQlearning(state)
        return action
    
    def fromStateToRender(self,state):
        from  GridWorld.GWEnvironnement import GWEnvironnement
        grid_shape = state[0]
        env = GWEnvironnement(grid_shape=grid_shape,entities=state[1:])
        return env.render()
        
    
    def update(self, state, reward, done, action, next_state):
        self.GWDeepQlearning.update(state, action, reward, next_state, done)