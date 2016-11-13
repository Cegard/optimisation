# -*- coding: utf-8 -*-

class Heuristic:
	
	def __init__(self, estimation_function_, parameters_):
		self.estimation_function = estimation_function_
		self.parameters = parameters_
	
	def estimate(*arguments):
		heuristic_arguments = dict(zip(self.parameters, arguments))
		return self.estimation_function(**heuristic_arguments)