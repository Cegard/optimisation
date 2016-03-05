# -*- coding: utf-8 -*-
from helpers import deepcopy, check_opposites


def iterated_dfs(puzzle):
    reached = puzzle.is_sorted()
    bottom = 0
    expanded_nodes = 0
    
    while not reached:
        bottom += 1
        print(bottom)
        level = 1
        nodes_stack = [(deepcopy(puzzle), level, '')]
        
        while nodes_stack != [] and not reached:
            visited_states = []
            last_one = nodes_stack.pop()
            node, node_level, previous_move = last_one[0], last_one[1], last_one[2]
            reached = node.is_sorted()
            
            if not reached and node_level < bottom:
                expanded_nodes += 1
                
                for move in node.possible_moves:
                    
                    if not check_opposites(previous_move, move):
                        node_to_add = deepcopy(node)
                        node_to_add.swap(move)
                        
                        if node_to_add not in visited_states:
                            nodes_stack.append((node_to_add, node_level+1, move))
                            visited_states.append(node_to_add)
        
    return expanded_nodes