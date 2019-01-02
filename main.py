#!/usr/bin/env python

from agent import *
from flappy import *
random.seed(5555)

agents = generate_population(8,5555)
agent=agents[0]

begin()
while True:
    begin2()
    movementInfo = showWelcomeAnimation()
    crashInfo = mainGame(movementInfo, agent.movements)
    agent.fitness = crashInfo['score']
    showGameOverScreen(crashInfo)
