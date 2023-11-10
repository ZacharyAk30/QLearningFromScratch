# make a grid world environment

import numpy as np
from Environnement import Environnement
from GridWorld.Entities import Entities,EntitiesList,Agent

class GWEnvironnement(Environnement):
    def __init__(self,grid_shape:tuple,entities:list[Entities]):
        self.grid_shape = grid_shape
        self.entities = entities
        self.world = self.create_world()
        self.finish = False        

    def create_world(self):
        world = [[0 for i in range(self.grid_shape[0])] for j in range(self.grid_shape[1])]
        for entity in self.entities:
            if entity.type == "agent":
                self.agent_pos = entity.position
            world[entity.position[0]][entity.position[1]] = entity
        return world
        
    def applyAction(self, action):
        x , y  = action[0] , action[1]
        new_agent_pos_x , new_agent_pos_y  = self.agent_pos[0] + x, self.agent_pos[1] + y
        reward = 0
        out_of_grid = new_agent_pos_x >= self.grid_shape[0] or new_agent_pos_x < 0 or new_agent_pos_y >= self.grid_shape[1] or new_agent_pos_y < 0
        if out_of_grid:
            reward = -999
        elif type(self.world[new_agent_pos_x][new_agent_pos_y]) in EntitiesList:
            entity = self.world[new_agent_pos_x][new_agent_pos_y]
            if entity.type == "goal":
                self.finish = True
            reward = entity.reward
            self.world[self.agent_pos[0]][self.agent_pos[1]] = 0
            self.world[new_agent_pos_x][new_agent_pos_y] = Agent((new_agent_pos_x,new_agent_pos_y))
            self.agent_pos = [new_agent_pos_x,new_agent_pos_y]
        else:
            self.world[self.agent_pos[0]][self.agent_pos[1]] = 0
            self.world[new_agent_pos_x][new_agent_pos_y] = Agent((new_agent_pos_x,new_agent_pos_y))
            self.agent_pos = [new_agent_pos_x,new_agent_pos_y]
        state = self.getState()
        return state , reward ,self.finish
        
    def getState(self):
        state = [self.grid_shape]
        for i in self.world:
            for j in i:
                if type(j) in EntitiesList:
                    state.append(j)
        return state
        
    def render(self):
    # return string self.world that represent the world where entities is aligned with the grid 
        string = ""
        for i in self.world:
            for j in i:
                if j == 0:
                    string += " . "  # open space
                elif str(j) == 'wall':
                    string += " W "  # wall
                elif str(j) == 'trap':
                    string += " T "  # trap
                elif str(j) == 'goal':
                    string += " G "  # goal
                elif str(j) == 'agent':
                    string += " A "  # goal
                else:
                    string += str(j)
            string += "\n"
        return string
    
    def isfiniish(self):
        for i in self.world:
            for j in i:
                if type(j) == Entities:
                    if j.type == "goal":
                        return True
        return False

