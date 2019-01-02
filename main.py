#!/usr/bin/env python

from agent import *
from flappy import *
random.seed(5555)

agents = generate_population(8)
agent=agents[0]
generations=1000

def evaluate(agents):
    for agent in agents:
        agent.mutate()

        begin2()
        movementInfo = showWelcomeAnimation()
        crashInfo = mainGame(movementInfo, agent.movements)
        
        agent.fitness = crashInfo['score']
        showGameOverScreen(crashInfo)
        print('fitness', agent.fitness)

def replace(agents):
    best = Agent.selection(agents, 'best')
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
        print('new generation')

if __name__=='__main__':
	main()
