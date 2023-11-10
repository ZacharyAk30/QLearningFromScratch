# Description: Markov chain
#                                    _________________________________
#                                   |                                 |
#                  |--------------->|                                 |
#                  |                |              Agent              |
#                  |       |------->|                                 |--------|
#                  |       |        |_________________________________|        |
#                  |       |                                                   |
#                  |       |                                                   |
#   State (s)      |       | Rewards (r)                                       | Actions (a)
#                  |       |                                                   |
#                  |       |        _________________________________          |
#                  |       |       |                                 |         |
#                  |       --------|                                 |         |
#                  |               |           Environnement         |<--------|
#                  ----------------|                                 |         
#                                  |_________________________________|         

from Environnement import Environnement
from Agent import Agent

class MarkovChain:
    def __init__(self):
        self.environnement = Environnement()
        self.agent = Agent()
        
    def step(self):
        # get the state
        state = self.environnement.getState()
        # get the action
        action = self.agent.getAction(state)
        # apply the action to the environnement
        state , reward = self.environnement.applyAction(action)
        # update the agent
        self.agent.update(state,reward)