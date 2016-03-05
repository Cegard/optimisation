# -*- coding: utf-8 -*-
from copy import deepcopy


def iterated_dfs(puzzle):
    reached = puzzle.is_sorted()
    bottom = 0
    expanded_nodes = 0
    
    while not reached:
        bottom += 1
        level = 1
        nodes_stack = [(deepcopy(puzzle), level)]
        print(bottom)
        while nodes_stack != [] and not reached:
            last_one = nodes_stack.pop()
            node, node_level = last_one[0], last_one[1]
            reached = node.is_sorted()
            
            if not reached and node_level < bottom:
                expanded_nodes += 1
                
                for move in node.possible_moves:
                    node_to_add = deepcopy(node)
                    node_to_add.swap(move)
                    nodes_stack.append((node_to_add, node_level+1))
        
    return expanded_nodes