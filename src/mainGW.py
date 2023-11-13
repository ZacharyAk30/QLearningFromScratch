from GridWorld.GWAgent import GridWorldAgent
from GridWorld.GWEnvironnement import GWEnvironnement
from markovchaine import MarkovChain
from GridWorld import GWEntities

recapPath = r".\src\GridWorld\recap\\"
modelPath = r".\src\GridWorld\model\\"

def episode(num_ep ,model_weights_path="GWDeepQlearning",recap_path="recap",policy="Qlearning",epsilon=0.1):
    currRecapPath = recapPath + recap_path + "-" + str(num_ep) + ".txt"
    currModelPath = modelPath + model_weights_path + "-" + str(num_ep) + ".pth"
    
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
    agent = GridWorldAgent(grid_size=grid_shape,num_entities=len(entity_list),policy=policy,epsilon=epsilon)
    if num_ep > 0:
        ModelPath = modelPath + model_weights_path + "-" + str(num_ep - 1) + ".pth"
        agent.GWDeepQlearning.load_model(ModelPath)
    markovchain = MarkovChain(agent,env)
    finish = False
    recap = []
    recap_action = []
    recap_reward = []
    cumlative_reward = 0
    step_count = 0
    while not finish:
        state , reward , finish,action = markovchain.step()
        cumlative_reward += reward
        recap.append(env.render())
        recap_action.append("action : "+str(action))
        recap_reward.append("reward : "+str(cumlative_reward))
        step_count += 1
        if step_count > 3000:
            finish = True
    step_count = 0
    with open(currRecapPath, 'w') as f:
        for world,action,reward in zip(recap,recap_action,recap_reward):
            f.write("step : " + str(step_count) + "\n")
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
            f.write(action + "\n")
            f.write(world + "\n")
            f.write(reward + "\n")
            f.write("--------------------" + "\n")
            step_count += 1
    agent.GWDeepQlearning.save_model(currModelPath)
    return cumlative_reward
        
if __name__ == "__main__":
    epsilon_start = 1.0
    epsilon_end = 0.01
    total_episodes = 10000
    start_episode = 0
    start = 9170
    slope = (epsilon_end - epsilon_start) / (total_episodes - start_episode)
    for i in range(start, total_episodes):
        epsilon = epsilon_start + slope * (i - start_episode)
        r = episode(i, epsilon=epsilon)
        print(f"Episode {i} - Epsilon {epsilon:.5f} - Reward {r}")