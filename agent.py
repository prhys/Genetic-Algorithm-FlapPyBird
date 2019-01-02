#!/usr/bin/env python

from random import random, randint, uniform, choice
import time

class Agent:
	jump_probab=0.07
	def __init__(self, length=8):
		self.movements = []
		self.fitness=uniform(0,20)

		for i in range(length):
			self.append_new_value()

	def __repr__(self):
		return '\nFlappy Bird agent:\n{} movements: {}\nFitness: {}\n'.format(
			    len(self.movements), self.movements, self.fitness)

	def __add__(self, agent2):
		index=randint(0, len(self.movements)-1)
		children = [Agent.frommovements(self.movements[:index]+agent2.movements[index:]),
		            Agent.frommovements(agent2.movements[:index]+self.movements[index:])]
		return children

	# @property
	# def fitness(self):
	# 	t1=time.time()


	def append_new_value(self):
		"""Append a new value to the movements list"""
		if random() < Agent.jump_probab:
			#The appended value will be True or False depending on random()
			self.movements.append(True)
		else:
			self.movements.append(False)

	def mutate(self, mutation_rate=None):
		"""The agent changes in a random fashion"""
		if mutation_rate == None:
			mutation_rate = 1/32*len(self.movements)

		if random() <= mutation_rate:
			#Only proceed if random() is lower than the mutation rate
			if random() < 0.5:
				self.append_new_value()
			else:
				#We didn't append anything to the list, so we will change randomly
				#one value of the list
				trues = [i for i, value in enumerate(self.movements) if value ==True]
				falses = [i for i, value in enumerate(self.movements) if value ==False]
				self.movements[choice(trues)] = False
				self.movements[choice(falses)] = True

	@staticmethod
	def crossbred(agents):
		"""Several agents randomly share characteristics in order to create
		new agents that might have their good traits"""
		return agents[0] + agents[1]

	@staticmethod
	def selection(agents, type='best'):
		"""For a random weighted selection of the best agents, choose best.
		Otherwise, choose worst"""
		assert type.lower()=='best' or type.lower()=='worst', "type must be 'best' or 'worst'"

		total=0
		chosen=[]
		def pie_selection(func):
			while True:
				target=uniform(0,total)
				position=0
				for i in agents:
					position+=func(i)
					if target<=position:
						if i not in chosen:
							chosen.append(i)
						break
				else:
					raise RuntimeError('selection pie is wrongly coded')
				if len(chosen)==2:
					break
		if type.lower()=='best':
			for i in agents:
				total+=i.fitness
			pie_selection(lambda agent: agent.fitness)
		else:
			for i in agents:
				total+=1/i.fitness
			pie_selection(lambda agent: 1/agent.fitness)
		for i in agents:
			print(i.fitness)
		print('chosen:',chosen[0].fitness, chosen[1].fitness)
		return chosen

	@classmethod
	def frommovements(cls, movements):
		agent=cls(0)
		agent.movements = movements
		return agent

def generate_population(population=8, length=8):
	agents=[]
	for i in range(population):
		agents.append(Agent(length))
	return agents

if __name__=='__main__':
	pop=generate_population()
	for i in pop:
		print('population', i.fitness)
	for i in Agent.selection(pop, 'worst'):
		print('best', i.fitness)
