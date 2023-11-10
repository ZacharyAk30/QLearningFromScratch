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
    def __init__(self,agent : Agent,env : Environnement):
        self.environnement = env
        self.agent = agent
        
    def step(self):
        state = self.environnement.getState()
        action = self.agent.getAction(state)
        state , reward , finish = self.environnement.applyAction(action)
        self.agent.update(state,reward)
        return state , reward , finish