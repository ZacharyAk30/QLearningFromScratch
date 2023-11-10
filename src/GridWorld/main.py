from MarkovProperty import MarkovProperty
from GridWorld.GWAgent import GridWorldAgent
from GridWorld.GWEnvironnement import GWEnvironnement
from markovchaine import MarkovChain
import Entities

if __name__ == '__main__':
    grid_shape = (10,10)
    entity_list = [
        Entities.Agent((0,0)),
        Entities.Goal((9,9)),
        Entities.Wall((3,2)),
        Entities.Wall((4,5)),
        Entities.Wall((9,5)),
        Entities.Wall((3,6)),
        Entities.Trap((3,3)),
    ]
    env = GWEnvironnement(grid_shape,entity_list)
    agent = GridWorldAgent()
    
    markovchain = MarkovChain(agent,env)
    finish = False
    while not finish:
        recap = []
        state , reward , finish = markovchain.step()
        recap.append(env.render())
    step_count = 0
    for i in recap:
        print("step : ",step_count)
        print(i)
        
        
    