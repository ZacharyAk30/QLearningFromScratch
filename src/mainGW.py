from GridWorld.GWAgent import GridWorldAgent
from GridWorld.GWEnvironnement import GWEnvironnement
from markovchaine import MarkovChain
from GridWorld import GWEntities

if __name__ == '__main__':
    grid_shape = (5,5)
    entity_list = [
        GWEntities.Agent((0,0)),
        GWEntities.Goal((4,4)),
        GWEntities.Wall((3,2)),
        GWEntities.Wall((4,2)),
        GWEntities.Wall((1,4)),
        GWEntities.Wall((3,1)),
        GWEntities.Trap((3,3)),
    ]
    env = GWEnvironnement(grid_shape,entity_list)
    agent = GridWorldAgent(grid_size=grid_shape,num_entities=len(entity_list),policy="humain")
    markovchain = MarkovChain(agent,env)
    finish = False
    recap = []
    recap_action = []
    recap_reward = []
    cumlative_reward = 0
    step_count = 0
    while not finish:
        print("step : ",step_count)
        state , reward , finish,action = markovchain.step()
        cumlative_reward += reward
        recap.append(env.render())
        recap_action.append("action : "+str(action))
        recap_reward.append("reward : "+str(cumlative_reward))
        step_count += 1
        if step_count > 100:
            finish = True
    step_count = 0
    for world,action,reward in zip(recap,recap_action,recap_reward):
        print("step : ",step_count)
        if action == f"action : {str([0,-1])}":
            action = "left"
        if action == f"action : {str([0,1])}":
            action = "right"
        if action == f"action : {str([1,0])}":
            action = "down"
        if action == f"action : {str([-1,0])}":
            action = "up"
        if action == f"action : {str([0,0])}":
            action = "stay" 
        print(action)
        print(world)
        print(reward)
        print("--------------------")
        step_count += 1
        
        
