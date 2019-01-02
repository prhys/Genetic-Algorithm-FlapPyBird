#!/usr/bin/env python

class Agent:
	def __init__(self):
	    self.agent='Agent'

	@property
	def fitness(self):
		fitness=-1
		return fitness

	def mutate(self):
		"""The agent changes in a random fashion"""
		pass

	@staticmethod
	def crossbred(agents):
		"""Several agents randomly share characteristics in order to create
		new agents that might have their good traits"""
		return agents[0:2]

	@staticmethod
	def selection(agents, type='best'):
		"""For selection of the best agents, choose best.
		Otherwise, choose worst"""
		assert type.lower()=='best' or type.lower()=='worst', "type must be 'best' or 'worst'"

		if type.lower()=='best':
			agents.sort(key=lambda agent: agent.fitness, reverse=True)
			return agents[0:2]
		
		else:
			agents.sort(key=lambda agent: agent.fitness)
			return agents[0:2]

def generate_population(population=8):
	agents=[]
	for i in range(population):
		agents.append(Agent())
	return agents

def death(agents):
	worst = Agent.selection(agents, type='worst')
	for i in worst:
		agents.remove(i)
	return agents

def birth(agents):
	best = Agent.selection(agents, type='best')
	for i in best:
		agents.append(i)
	return agents


if __name__=='__main__':
	print(Agent().agent)
