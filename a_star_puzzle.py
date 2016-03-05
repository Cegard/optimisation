# -*- coding: utf-8 -*-
from puzzle import Puzzle
from idfs import iterated_dfs as i_dfs
import helpers

puzzle_length = 4
puzzle = Puzzle(puzzle_length)
puzzles = {10: [], 15: [], 20: [], 25: []}

#disorders the puzzle
for key in puzzles:
    
    for i in range(30):
        puzzles[key].append(helpers.disorder_puzzle(key, puzzle))

# assigns the same disorded puzzles to the lists to be ran for the respective algorithm
idfs_puzzles = helpers.deepcopy(puzzles)
h1_puzzles = helpers.deepcopy(puzzles)
h2_puzzles = helpers.deepcopy(puzzles)

# gets the results
idfs_results = helpers.run_algorithm(idfs_puzzles, i_dfs)
h1_results = []
h2_results = []

#computes results
for key in idfs_results:
    