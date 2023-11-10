# make a grid world environment

import numpy as np
from Environnement import Environnement
from Entities import Entities

class GWEnvironnement(Environnement):
    def __init__(self,grid_shape:tuple,entities:list[Entities]):
        self.grid_shape = grid_shape
        self.entities = entities
        self.world = self.create_world()
        self.finish = False        

    def create_world(self):
        world = np.zeros(self.grid_shape)
        for entity in self.entities:
            if entity.type == "agent":
                self.agent_pos = entity.position
            world[entity.position[0],entity.position[1]] = entity
        return world
        
    def applyAction(self, action):
        x , y  = action[0] , action[1]
        new_agent_pos_x , new_agent_pos_y  = self.agent_pos[0] + x, self.agent_pos[1] + y
        out_of_grid = new_agent_pos_x >= self.grid_shape[0] or new_agent_pos_x < 0 or new_agent_pos_y >= self.grid_shape[1] or new_agent_pos_y < 0
        if out_of_grid:
            reward = -999
            
        if type(self.world[new_agent_pos_x,new_agent_pos_y]) == Entities:
            entity = self.world[new_agent_pos_x,new_agent_pos_y]
            if entity.type == "goal":
                self.finish = True
            reward = entity.reward
            self.world[self.agent_pos[0],self.agent_pos[1]] = 0
            self.world[new_agent_pos_x,new_agent_pos_y] = entity
        state = self.getState()
        return state , reward ,self.finish
        
    def getState(self):
        state = []
        for i in self.world:
            for j in i:
                if type(j) == Entities:
                    state.append(j)
        return state
        
    def render(self):
        return self.world
    
    def isfiniish(self):
        for i in self.world:
            for j in i:
                if type(j) == Entities:
                    if j.type == "goal":
                        return True
        return False

