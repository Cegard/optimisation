# -*- coding: utf-8 -*-
from copy import deepcopy
from random import randint as rand


def list_add(lst, item):
    """
    Appends the given item to the given list, and returns the item
    :param lst: A list object.
    :param item: The item to be added
    :returns: The same given item
    """
    y = []
    
    lst.append(item)
    return deepcopy(item)


def disorder_puzzle(movements, puzzle):
    """"
    Makes the given number of random movements on the given puzzle
    :param movements: The movements to make on the puzzle
    :param puzzle: The puzzle to disorder
    :returns: a copy of the given puzzle idsordered
    """
    directions = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    opposites = {0: 1, 1: 0, 2: 3, 3: 2}
    copied_puzzle = deepcopy(puzzle)
    
    
    def get_availability(key):
        return copied_puzzle.possibilities[key] \
                and copied_puzzle.previous_move != directions[opposites[key]]
    
    
    for i in range(movements):
        direction = rand(0, 3)
        can_move = get_availability(direction)
        
        while(not can_move):
            direction += 1
            can_move = get_availability(direction%4)
        
        copied_puzzle.swap(directions[direction%4])
    
    return copied_puzzle


def run_algorithm(puzzles, algorithm):
    results = dict()
    
    for random_movements in puzzles:
        expanded_nodes = []
        
        for puzzle in puzzles[random_movements]:
            expanded_nodes.append(algorithm(puzzle))
            results[random_movements] = expanded_nodes
    
    return results