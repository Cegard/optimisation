# -*- coding: utf-8 -*-
from node import Node
from estimatees import nodes_names, tasks_names
    
def define_search_node(name, task, f):
    return lambda x: x.name == name and x.task == task and x.f_value < f

def get_parents(node):
    
    while node:
        yield node
        node = node.parent

def a_star():
    first_node = Node(name = None, task = None, parent = None)
    open_list = [first_node] # state, F, G, H, parent, last move
    closed_list = []
    reached = False
    goal = None
    bottom = len(tasks_names)
    
    while not reached:
        q_node = min(open_list, key = lambda a_node: a_node.f_value)
        open_list.remove(q_node)
        excluded_nodes = set()
        
        for previous_node in get_parents(q_node):
            excluded_nodes.add(previous_node.name)
        successors = (Node(name = n, task = tasks_names[q_node.depth], parent = q_node)
                      for n in set(nodes_names) - excluded_nodes)
        
        for successor in successors:
            search_function = define_search_node(name = successor.name,
                                                 task = successor.task,
                                                 f = successor.f_value)
            is_the_bottom = successor.depth == bottom
            has_to_skip_node = False
            if not is_the_bottom:
                
                if True not in  (map(search_function, open_list)) and \
                        True not in (map(search_function, closed_list)):
                    open_list.append(successor)
            
            else:
                goal = successor
        
        closed_list.append(q_node)
        reached = goal is not None or open_list == []
    
    return get_parents(goal)