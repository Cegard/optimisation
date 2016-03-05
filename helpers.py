# -*- coding: utf-8 -*-
from statistics import mean, median, stdev
from copy import deepcopy
from random import randint as rand

directions = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
opposites = {'up': 1, 'down': 0, 'left': 3, 'right': 2}


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
    global directions, opposites
    copied_puzzle = deepcopy(puzzle)
    
    
    def get_availability(key):
        return copied_puzzle.possibilities[key] \
                and not check_opposites(copied_puzzle.previous_move, directions[key])
    
    
    for i in range(movements):
        direction = rand(0, 3)
        can_move = get_availability(direction)
        
        while(not can_move):
            direction += 1
            can_move = get_availability(direction%4)
        
        copied_puzzle.swap(directions[direction%4])
    
    return copied_puzzle


def run_algorithm(puzzles, algorithm, heuristic = None):
    results = dict()
    
    for random_movements in puzzles:
        expanded_nodes = []
        
        for puzzle in puzzles[random_movements]:
            expanded_nodes.append(algorithm(puzzle) if not heuristic else algorithm(puzzle, heuristic))
            results[random_movements] = expanded_nodes
    
    return results


def check_opposites(previous_move, next_move):
    global directions, opposites
    return previous_move == directions[opposites[next_move]]


def find_min_by_pos(index, lst):
    """
    Finds the object of all in the given list, checking only at the given index
    :param index: the index in where to look to find the min
    :param *lst: collection of objects
    :returns: a *lst member
    """
    min_of_all = {index: float('inf')}
    
    for tpl in lst:
        
        if tpl[index] <= min_of_all[index]: min_of_all = tpl
    
    return min_of_all


def is_in(member, lsts, index):
    lst_length = len(lsts)
    actual_index = 0
    found_index = -1
    
    while((actual_index < lst_length) and (lsts != [])):
        was_found = lsts[actual_index][index] == member
        
        if was_found:
            found_index = actual_index
            actual_index = lst_length
        
        actual_index += 1
    
    return found_index


def calc_manhattan(puzzle):
    total = 0
    
    for row in range(puzzle.length):
        
        for col in range(puzzle.length):
            tile = puzzle.board[row][col]
            
            if tile != None: 
                tile -= 1
                total += abs(row - tile//puzzle.length)
                total += abs(col - tile%puzzle.length)
    
    return total

def computes_results(results):
    computes = dict()
    
    for moves in results:
        computes[moves] = dict()
        computes[moves]['mean'] = mean(results[moves])
        computes[moves]['median'] = median(results[moves])
        computes[moves]['mean_stdev'] = stdev(results[moves], computes[moves]['mean'])
        computes[moves]['median_stdev'] = stdev(results[moves], computes[moves]['median'])
    
    return computes


def print_results(results, algorithm):
    message = '-'*20 +'\nresults of '+algorithm+': \n'
    print(message)
    
    for moves in results:
        
        for value in moves:
            sub_message = value + ': ' + results[moves][value]
            print(sub_message)