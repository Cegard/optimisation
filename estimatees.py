# -*- coding: utf-8 -*-

def define_estimations(estimatees):
	
	def calculate_estimation(node, task):
		return estimatees[node]._asdict()[task]
	
	return calculate_estimation