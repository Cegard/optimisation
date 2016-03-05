# -*- coding: utf-8 -*-
from helpers import deepcopy, find_min_by_pos, check_opposites, is_in

def a_star_h1(puzzle, heuristic):
    copied_puzzle = deepcopy(puzzle)
    open_list = [(copied_puzzle, 0, 0, 0, None, '')] # state, F, G, H, parent, last move
    closed_list = []
    reached = copied_puzzle.is_sorted()
    expanded_nodes = 0
    
    while (not reached and open_list != []):
        index_to_find_min = 1
        last_node = find_min_by_pos(index_to_find_min, open_list)
        open_list.remove(last_node)
        closed_list.append(last_node)
        node = last_node[0]
        previous_move = last_node[5]
        actual_g_cost = last_node[2]
        reached = node.is_sorted()
        
        if not reached:
            expanded_nodes += 1
            
            for move in node.possible_moves:
                
                if not check_opposites(previous_move, move):
                    node_to_add = deepcopy(node)
                    node_to_add.swap(move)
                    index_to_is_in = 0
                    closed_index = is_in(node_to_add, closed_list, index_to_is_in)
                    
                    if closed_index == -1:
                        g = actual_g_cost+1
                        h = node_to_add.misplaceds
                        f = g+h
                        open_index = is_in(node_to_add, open_list, index_to_is_in)
                        
                        if open_index == -1:
                            open_list.append((node_to_add, f, g, h, node, move))
                        
                        else:
                            
                            if g < open_list[open_index][2]:
                                open_list[open_index][1] = f
                                open_list[open_index][2] = g
                                open_list[open_index][3] = h
                                open_list[open_index][4] = node
                                open_list[open_index][5] = move
        
    return expanded_nodes