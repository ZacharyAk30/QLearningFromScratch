# S : set of possible states
# A : set of possible actions
# R : distribution of reward given (state, action) pair
# P : transition probability i.e. distribution over next state given (state, action) pair
# G : discount factor

class MarkovProperty:
    S = None
    A = None
    R = None
    P = None
    G = None