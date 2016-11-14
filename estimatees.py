# -*- coding: utf-8 -*-
from collections import namedtuple

h_parameters = ['excluded_node', 'excluded_task']
nodes_names = ['node_A', 'node_B', 'node_C', 'node_D', 'node_E']
tasks_names = ['task_A', 'task_B', 'task_C', 'task_D']
Estimatees = namedtuple('Estimatees', tasks_names)
estimations = []
estimations.append(Estimatees(task_A = 8.299682107, task_B = 0.3482262,
							  task_C = 40.57335202, task_D = 5.867378787))
estimations.append(Estimatees(task_A = 3, task_B = 3, task_C = 2.029215707,
							  task_D = 20.84594702))
estimations.append(Estimatees(task_A = 6, task_B = 28, task_C = 3.603635456,
							  task_D = 14.01374164))
estimations.append(Estimatees(task_A = 70, task_B = 8.699567797,
							  task_C = 70.47944404, task_D = 41.92349852))
estimations.append(Estimatees(task_A = 7, task_B = 3.555243475, task_C = 39.95905269,
							  task_D = 1.893329623))
estimations_per_node = dict(zip(nodes_names, estimations))

def get_time(node, task):
	return estimations_per_node[node]._asdict()[task]

def get_estimation(excluded_node, excluded_task):
	return min(get_time(node, task) for node in set(nodes_names)-{excluded_node}
			   for task in set(tasks_names)-{excluded_task})