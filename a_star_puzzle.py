#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint as rand
from copy import deepcopy as copy
from puzzle import Puzzle


def disorder_puzzle(movements, puzzle):
    directions = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    opposites = {0: 1, 1: 0, 2: 3, 3: 2}
    copied_puzzle = copy(puzzle)
    
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


puzzle_length = 4
puzzle = Puzzle(puzzle_length)
puzzles = {10: [], 15: [], 20: [], 25: []}

for key in puzzles:
    
    for i in range(30):
        puzzles[key].append(disorder_puzzle(key, puzzle))

disorder_puzzle(25, puzzle)
ids_puzzles = copy(puzzles)
h1_puzzles = copy(puzzles)
h2_puzzles = copy(puzzles)