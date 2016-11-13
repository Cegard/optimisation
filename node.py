# -*- coding: utf-8 -*-

class Node:
	
	def __init__(self, name_, heuristic):
		self.name = name_
		self.__task = None
		self.__estimated_time = None
		self.__real_time = None
		self.__heuristic = heuristic
	
	@property
	def task(self):
		return self.__task
	
	@property
	def estimated_time(self):
		return self.__estimated_time
	
	@property
	def estimated_time(self):
		return self.__estimated_time
	
	@task.setter
	def task(self, task):
		self.__estimated_time = self.__heuristic.estimate(self.name, task.name)
		self.__real_time = self.__estimated_time + 0.7
		self.__task = task