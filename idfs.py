# -*- coding: utf-8 -*-
from copy import deepcopy


def iterated_dfs(puzzle):
    reached = puzzle.is_ordered()
    bottom = 0
    directions = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    
    while not reached:
        bottom += 1
        level = 0
        nodes_stack = [deepcopy(puzzle)]
        
        while not reached and nodes_stack != []:
            level += 1
            last_visited = nodes_stack.pop()
            reached = last_visited.is_ordered()
            
            if not reached and level < bottom:
                nodes_stack += [last_visited.swap(d) for d in range(4) if last_visited.possibilities[directions[d]]]