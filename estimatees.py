# -*- coding: utf-8 -*-
from collections import namedtuple

h_parameters = ['excluded_node', 'excluded_task']
nodes_names = ['node_A', 'node_B', 'node_C', 'node_D', 'node_E']
tasks_names = ['task_A', 'task_B', 'task_C', 'task_D']
Estimatees = namedtuple('Estimatees', tasks_names)
estimations = []
node_a = Estimatees(task_A = 8.299682107, task_B = 7.3482262,
					task_C = 40.57335202, task_D = 79.86737879)
node_b = Estimatees(task_A = 3.287770817, task_B = 2.96341577,
					task_C = 21.02921571, task_D = 50.84594702)
node_c = Estimatees(task_A = 6.091965466, task_B = 5.995993128,
					task_C = 35.60363546, task_D = 61.01374164)
node_d = Estimatees(task_A = 19.520565, task_B = 16.6995678,
					task_C = 70.47944404, task_D = 91.92349852)
node_e = Estimatees(task_A = 6.626101157, task_B = 5.555243475,
					task_C = 39.95905269, task_D = 64.89332962)
estimations.append(node_a)
estimations.append(node_b)
estimations.append(node_c)
estimations.append(node_d)
estimations.append(node_e)
estimations_per_node = dict(zip(nodes_names, estimations))

def get_time(node, task):
	return estimations_per_node[node]._asdict()[task]


def get_estimation(excluded_node, excluded_task):
	return min(get_time(node, task) for node in set(nodes_names)-{excluded_node}
			   for task in set(tasks_names)-{excluded_task})