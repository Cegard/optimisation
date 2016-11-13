# -*- coding: utf-8 -*-
from task import Task
from node import Node
from heuristic import Heuristic
from collections import namedtuple
from estimatees import define_estimations

if __name__ == "__main__":
	
	fields = ['task_A', 'task_B', 'task_C', 'Task_D']
	Estimatees = namedtuple('Estimatees', fields)
	estimations_node_a = Estimatees(8.299682107, 0.3482262, 40.57335202, 5.867378787)
	estimations_node_b = Estimatees(3, 3, 2.029215707, 20.84594702)
	estimations_node_c = Estimatees(6, 28, 3.603635456, 14.01374164)
	estimations_node_d = Estimatees(70, 8.699567797, 70.47944404, 41.92349852)
	estimations_node_e = Estimatees(7, 3.555243475, 39.95905269, 1.893329623)
	estimations = {'node_A': estimations_node_a, 'node_B': estimations_node_b,
				   'node_C': estimations_node_c, 'node_D': estimations_node_d,
				   'node_E': estimations_node_e}
	estimate = define_estimations(estimations)
	h_parameters = ['node', 'task']
	heuristic = Heuristic(estimate, )