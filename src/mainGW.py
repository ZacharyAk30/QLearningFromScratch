from GridWorld.GWAgent import GridWorldAgent
from GridWorld.GWEnvironnement import GWEnvironnement
from markovchaine import MarkovChain
from GridWorld import Entities

if __name__ == '__main__':
    grid_shape = (5,5)
    entity_list = [
        Entities.Agent((0,0)),
        Entities.Goal((4,4)),
        Entities.Wall((3,2)),
        Entities.Wall((4,2)),
        Entities.Wall((1,4)),
        Entities.Wall((3,1)),
        Entities.Trap((3,3)),
    ]
    env = GWEnvironnement(grid_shape,entity_list)
    agent = GridWorldAgent(policy="humain")
    markovchain = MarkovChain(agent,env)
    finish = False
    recap = []
    recap_action = []
    recap_reward = []
    cumlative_reward = 0
    while not finish:
        state , reward , finish,action = markovchain.step()
        cumlative_reward += reward
        recap.append(env.render())
        recap_action.append("action : "+str(action))
        recap_reward.append("reward : "+str(cumlative_reward))
    step_count = 0
    for world,action,reward in zip(recap,recap_action,recap_reward):
        print("step : ",step_count)
        print(action)
        print(world)
        print(reward)
        step_count += 1
        
        
    