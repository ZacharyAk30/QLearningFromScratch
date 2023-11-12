import torch
from GridWorld.GWProperty import TranslateEntities
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class GWDeepQlearning:
    def __init__(self, grid_size, hidden_dim=64 , lr=0.05, gamma=0.99,epsilon=0.1):
        self.gamma = gamma
        self.grid_size = grid_size
        self.replay_buffer = buffer
        self.action_to_int = {
            (0, -1): 0, 
            (0, 1): 1, 
            (1, 0): 2, 
            (-1, 0): 3, 
        }
        self.action_to_list = {
            0: [0, -1], 
            1: [0, 1], 
            2: [1, 0], 
            3: [-1, 0],        
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

    def update(self, state:list, action:list, reward:int, next_state:list, done:bool, batch_size:int = 128):
        # Store the transition in the replay buffer
        # This includes the current state, action taken, reward received, next state, and whether the episode ended
        self.replay_buffer.push(state, action, reward, next_state, done)

        # Only update the network if we have enough samples in the replay buffer
        # This is to ensure that we have enough data to learn effectively
        if len(self.replay_buffer) < batch_size:
            return

        # Sample a minibatch from the replay buffer
        # This is a random selection of transitions used to update the network
        minibatch = self.replay_buffer.sample(batch_size)

        # Unpack the minibatch
        # This separates the minibatch into individual components
        states, actions, rewards, next_states, dones = zip(*minibatch)

        # Process the states and next_states
        # This converts the states and next states into a format that the network can accept
        states = torch.stack([self._process_state(state) for state in states])
        next_states = torch.stack([self._process_state(next_state) for next_state in next_states])

        # Convert the rest to tensors
        # This converts the actions, rewards, and "done" flags into tensors for processing by the network
        rewards = torch.tensor(rewards, dtype=torch.float)
        actions = torch.tensor([self.action_to_int[tuple(action)] for action in actions], dtype=torch.long)
        dones = torch.tensor(dones, dtype=torch.float)

        # Get the current Q-values by passing the states through the network
        q_values = self.model(states)
        # Get the next Q-values by passing the next states through the network
        next_q_values = self.model(next_states)

        # Get the Q-value of the action taken
        q_value = q_values.gather(1, actions.unsqueeze(1)).squeeze(1)
        # Get the maximum Q-value for the next state
        next_q_value = next_q_values.max(1)[0]
        # Calculate the expected Q-value
        expected_q_value = rewards + self.gamma * next_q_value * (1 - dones)

        # Calculate the loss between the current and expected Q-values
        loss = self.criterion(q_value, expected_q_value.detach())
        # Zero the gradients before backpropagation
        self.optimizer.zero_grad()
        # Backpropagate the loss
        loss.backward()
        # Update the network weights
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
    
    def save_model(self, path):
        torch.save(self.model.state_dict(), path)
    def load_model(self, path):
        self.model.load_state_dict(torch.load(path))
    


import random
from collections import deque

class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
        if len(self.buffer) > 100000:
            print("buffer full")

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)

buffer = ReplayBuffer(100000)
# Dans votre classe GWDeepQlearning, vous initialiserez ensuite le ReplayBuffer :
# self.replay_buffer = ReplayBuffer(capacity)

# Et dans votre méthode update, vous feriez quelque chose comme ceci :
# if len(self.replay_buffer) > batch_size:
#     minibatch = self.replay_buffer.sample(batch_size)
#     # Décompressez le minibatch et utilisez-le pour l'entraînement