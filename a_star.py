# -*- coding: utf-8 -*-
from helpers import deepcopy, find_min_by_pos, check_opposites, is_in

def a_star_h1(puzzle):
    copied_puzzle = deepcopy(puzzled)
    open_list = [(copied_puzzle, 0, 0, 0, None, '')] # state, F, G, H, parent, last move
    closed_list = []
    reached = copied_puzzle.is_sorted()
    
    while (not reached or open_list != []):
        last_node = find_min_by_pos(*open_list, index = 1)
        open_list.remove(last_node)
        closed_list.append(last_node)
        node = last_node[0]
        previous_move = last_node[5]
        actual_g_cost = last_node[2]
        
        for move in node.possible_moves:
            
            if not check_opposites(previous_move, move):
                node_to_add = deepcopy(node)
                node_to_add.swap(move)
                is_in_the_closed = is_in(node, closed_list, 0)[0]
                
                if not is_in_the_closed:
                    is_in_the_open = is_in(node, open_list, 0)
                    open_index = -1
                    g = actual_g_cost+1
                    h = node.misplaceds
                    f = g+h
                    
                    if not is_in_the_open[0]:
                        open_list.append((node_to_add, f, g, h, node, move))
                    
                    else:
                        
                        if is_in_the_open[1]