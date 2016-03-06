# -*- coding: utf-8 -*-
from puzzle import Puzzle
from idfs import iterated_dfs as i_dfs
from a_star import a_star
import helpers

puzzle_length = 4
number_of_puzzles = 30
puzzle = Puzzle(puzzle_length)
puzzles = {5: [], 15: [], 20: [], 25: []}

#disorders the puzzle
for key in puzzles:
    
    for i in range(number_of_puzzles):
        puzzles[key].append(helpers.disorder_puzzle(key, puzzle))


# assigns the same disorded puzzles to the lists to be ran for the respective algorithm
idfs_puzzles = helpers.deepcopy(puzzles)
h1_puzzles = helpers.deepcopy(puzzles)
h2_puzzles = helpers.deepcopy(puzzles)

# gets the results
heuristics={'h1': helpers.count_misplaceds, 'h2':helpers.calc_manhattan}
idfs_puzzles.pop(25) # since IDFS algorithm is too slow, it won't calculate for 25 moves puzzles
idfs_results = helpers.run_algorithm(idfs_puzzles, algorithm = i_dfs)
h1_results = helpers.run_algorithm(h1_puzzles, heuristics, 'h1', algorithm = a_star)
h2_results = helpers.run_algorithm(h1_puzzles, heuristics, 'h2', algorithm = a_star)

#computes results
idfs_computes = helpers.computes_results(idfs_results)
h1_computes = helpers.computes_results(h1_results)
h2_computes = helpers.computes_results(h2_results)

# shows results
print (idfs_computes)
helpers.print_results(idfs_computes, 'iterated-dfs')
helpers.print_results(h1_computes, 'A* h1')
helpers.print_results(h2_computes, 'A* h2')