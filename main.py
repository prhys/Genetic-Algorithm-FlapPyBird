#!/usr/bin/env python

from agent import *
from flappy import *

number_agents=8
agents = generate_population(8, 200)
agent=agents[0]
generations=1000

def evaluate(agents):
    for agent in agents:
        for l in range(len(agent.movements)):
            if agent.fitness>9000:
                agent.mutate()
            else:
           	    agent.mutate(mutation_rate=0.1)

        begin2()
        movementInfo = showWelcomeAnimation()
        t1=time.time()
        crashInfo = mainGame(movementInfo, agent.movements)
        t2=time.time()
        agent.fitness = 100*(t2-t1)+9000*crashInfo['score']
        showGameOverScreen(crashInfo)
        print('fitness', agent.fitness)

def replace(agents):
    best = Agent.selection(agents, 'best')
    print('best fitness', best[0].fitness, best[1].fitness)
    children = Agent.crossbred(best)
    worst = Agent.selection(agents, 'worst')
    for i in worst:
    	agents.remove(i)
    for i in children:
    	agents.append(i)

def main():
    begin()
    for i in range(generations):
        evaluate(agents)
        replace(agents)
        print('generation ', i+1)

if __name__=='__main__':
	main()
