import torch
from GridWorld.GWProperty import TranslateEntities
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class GWDeepQlearning:
    def __init__(self, grid_size, hidden_dim=64, lr=0.05, gamma=0.99,epsilon=0.1):
        self.gamma = gamma
        self.grid_size = grid_size
        self.action_to_int = {
            (0, -1): 0, 
            (0, 1): 1, 
            (1, 0): 2, 
            (-1, 0): 3, 
            (0, 0): 4 
        }
        self.action_to_list = {
            0: [0, -1], 
            1: [0, 1], 
            2: [1, 0], 
            3: [-1, 0], 
            4: [0, 0]       
        }
        total_grid_size = grid_size[0] * grid_size[1]
        input_shape = (total_grid_size + 1) * 4
        self.model = nn.Sequential(
            nn.Linear(input_shape, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, len(self.action_to_int))
        )
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()
        self.epsilon = epsilon

    def update(self, state:list, action:list, reward:int, next_state:list, done:bool):
        state = self._process_state(state)
        next_state = self._process_state(next_state)
        reward = torch.tensor(reward, dtype=torch.float)
        action = torch.tensor(self.action_to_int[tuple(action)], dtype=torch.long)

        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            reward = torch.unsqueeze(reward, 0)
            action = torch.unsqueeze(action, 0)
            done = (done, )

        q_values = self.model(state)
        next_q_values = self.model(next_state)

        q_value = q_values.gather(1, action.unsqueeze(1)).squeeze(1)
        next_q_value = next_q_values.max(1)[0]
        expected_q_value = reward + self.gamma * next_q_value * (1 - torch.tensor(done, dtype=torch.float))

        loss = self.criterion(q_value, expected_q_value.detach())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def __call__(self, state):
        state = self._process_state(state)
        if random.random() < self.epsilon:  # exploration 
            action =  random.choice(range(len(self.action_to_int)))
            return self.action_to_list[action]
        q_values = self.model(state) # policy
        action_index = np.argmax(q_values.detach().numpy())
        action = list(self.action_to_list)[action_index]
        action = self.action_to_list[action]
        return action
    
    def _process_state(self, state):
        grid_shape:tuple = state[0]
        grill_vector =[4,grid_shape[0],grid_shape[1],0]
        state_vector = [grill_vector]        
        for entitie in state[1:]:
            entitie_vector = []
            entitie_vector.append(TranslateEntities[entitie.type])
            entitie_vector.append(entitie.position[0])
            entitie_vector.append(entitie.position[1])
            entitie_vector.append(entitie.reward)
            state_vector.append(entitie_vector)
        state_vector = torch.tensor(state_vector, dtype=torch.float)
        return torch.flatten(state_vector)
    