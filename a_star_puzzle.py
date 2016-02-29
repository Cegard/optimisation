#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint as rand
from copy import deepcopy as copy
from puzzle import Puzzle


def disorder_puzzle(movements, puzzle):
    directions = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    copied_puzzle = copy(puzzle)
    
    for i in range(movements):
        direction = rand(0, 3)
        can_move = copied_puzzle.possibilities[direction]
        
        while(not can_move):
            direction += 1
            can_move = copied_puzzle.possibilities[direction%4]
        
        copied_puzzle.swap(directions[direction%4])
    
    return copied_puzzle


puzzle_length = 4
puzzle = Puzzle(puzzle_length)
puzzles = {10: [], 15: [], 20: [], 25: []}

for key in puzzles:
    
    for i in range(30):
        puzzles[key].append(disorder_puzzle(key, puzzle))

ids_puzzles = copy(puzzles)
h1_puzzles = copy(puzzles)
h2_puzzles = copy(puzzles)