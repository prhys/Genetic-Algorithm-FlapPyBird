#!/usr/bin/env python

from agent import *
from flappy import *

agents = generate_population(16, 200)
agent=agents[0]
generations=1000

def evaluate(agents):
    for agent in agents:
        if Agent.selection(agents)[0].fitness<100:
        	agent.mutate(mutation_rate=0.75)
        else:
        	agent.mutate()

        begin2()
        movementInfo = showWelcomeAnimation()
        t1=time.time()
        crashInfo = mainGame(movementInfo, agent.movements)
        t2=time.time()
        agent.fitness = (t2-t1)+100*crashInfo['score']
        showGameOverScreen(crashInfo)
        print('fitness', agent.fitness)

def replace(agents):
    best = Agent.selection(agents, 'best')
    print('best fitness', best[0].fitness)
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
        print(agents)

if __name__=='__main__':
	main()
