# -*- coding: utf-8 -*-
from node import Node
from estimatees import nodes_names, tasks_names


def define_search_node(name, task, f_value, depth):
    evaluate = lambda x : x.name == name and \
               x.task == task and x.depth == depth and x.f_value < f_value
    
    return evaluate


def check_existence(function, lst):
    return True in map(function, lst)


def get_track(node):
    
    while node:
        yield node
        node = node.parent


def a_star():
    first_node = Node(name = None, task = None, parent = None)
    open_list = [first_node]
    closed_list = []
    reached = False
    goal = None
    bottom = len(tasks_names)
    names = set(nodes_names)
    tasks = set(tasks_names)
    nodes = 0
    
    while not reached:
        q_node = min(open_list, key = lambda a_node: a_node.f_value)
        open_list.remove(q_node)
        excluded_names = set()
        excluded_tasks = set()
        is_the_bottom = q_node.depth == bottom
        
        if not is_the_bottom:
            nodes += 1
            
            for previous_node in get_track(q_node):
                excluded_names.add(previous_node.name)
                excluded_tasks.add(previous_node.task)
            
            successors = (Node(name = available_name, task = available_task, parent = q_node)
                          for available_name in names - excluded_names
                          for available_task in tasks - excluded_tasks)
            
            for successor in successors:
                arguments = {'name': successor.name,
                             'task': successor.task,
                             'f_value': successor.f_value,
                             'depth': successor.depth}
                
                search_function = define_search_node(**arguments)
                
                if not (check_existence(search_function, open_list) or \
                        check_existence(search_function, closed_list)):
                    open_list.append(successor)
            
            closed_list.append(q_node)
        
        else: goal = q_node
        
        reached = goal is not None or open_list == []
    
    print(nodes)
    return get_track(goal)