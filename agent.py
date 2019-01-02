#!/usr/bin/env python

from random import random, randint

class Agent:
	def __init__(self, length):
		self.movements = []

		for i in range(length):
			self.append_new_value()

	def append_new_value(self):
		"""Append a new value to the movements list"""
		if random() < 0.5:
			#The appended value will be True or False depending on random()
			self.movements.append(True)
		else:
			self.movements.append(False)

	@property
	def fitness(self):
		fitness=-1
		return fitness

	def mutate(self, mutation_rate=0.15):
		"""The agent changes in a random fashion"""
		if random() <= mutation_rate:
			#Only proceed if random() is lower than the mutation rate
			if random() < 0.5:
				self.append_new_value()
			else:
				#We didn't append anything to the list, so we will change randomly
				#one value of the list
				try:
					#randint() will raise an error if len(self.movements)==0
					#In this case, there's nothing to change.
					position=randint(0, len(self.movements)-1)
				except ValueError:
					pass
				else:
					if self.movements[position]:
						self.movements[position]=False
					else:
						self.movements[position]=True

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
	print(Agent(8).movements)