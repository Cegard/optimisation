# -*- coding: utf-8 -*-
from heuristic import Heuristic
from estimatees import get_time, get_estimation, h_parameters

class Node:
	
	__estimate = Heuristic(estimation_function = get_estimation,
						 parameters = h_parameters).estimate
	
	def __init__(self, name, task, parent):
		self.__name = name
		self.__task = task
		self.__parent = parent
		self.__g_value = get_time(node = name, task = task) + \
						 parent.__g_value if parent else 0
		self.__h_value = Node.__estimate(name, task)
		self.__f_value = self.__h_value + self.__g_value
		self.__depth = self.__parent.depth + 1 if parent else 0
	
	@property
	def name(self): return self.__name
	
	@property
	def task(self): return self.__task
	
	@property
	def parent(self): return self.__parent
	
	@property
	def g_value(self): return self.__g_value
	
	@property
	def h_value(self): return self.__h_value
	
	@property
	def f_value(self): return self.__f_value
	
	@property
	def depth(self): return self.__depth