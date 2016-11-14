# -*- coding: utf-8 -*-

class Heuristic:
	
	def __init__(self, estimation_function, parameters):
		self.estimation_function = estimation_function
		self.parameters = parameters
	
	def estimate(self, *arguments):
		heuristic_arguments = dict(zip(self.parameters, arguments))
		return self.estimation_function(**heuristic_arguments)