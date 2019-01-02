#!/usr/bin/env python

from random import random, randint
import time

class Agent:
	def __init__(self, length=8):
		self.movements = []
		self.fitness=-1

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


	def append_new_value(self, jump_probab=0.07):
		"""Append a new value to the movements list"""
		if random() < jump_probab:
			#The appended value will be True or False depending on random()
			self.movements.append(True)
		else:
			self.movements.append(False)

	def mutate(self, mutation_rate=0.35):
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
		return agents[0] + agents[1]

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
	print(generate_population())
