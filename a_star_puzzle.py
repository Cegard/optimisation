#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint as rand
from copy import deepcopy as copy
from puzzle import Puzzle


def disorder_toy(movements, toy):
    directions = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    copied_toy = copy(toy)
    
    for i in range(movements):
        direction = rand(0, 3)
        can_move = copied_toy._movements[direction]
        
        while(not can_move):
            direction += 1
            can_move = copied_toy._movements[direction%copied_toy._length]
        
        copied_toy.swap(directions[direction%copied_toy._length])
    
    return copied_toy


toy_length = 4
toy = Puzzle(toy_length)
puzzles = {10: [], 15: [], 20: [], 25: []}

for key in puzzles:
    
    for i in range(30):
        puzzles[key].append(disorder_toy(key, toy))

ids_puzzles = copy(puzzles)
h1_puzzles = copy(puzzles)
h2_puzzles = copy(puzzles)