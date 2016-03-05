# -*- coding: utf-8 -*-
from puzzle import Puzzle
from idfs import iterated_dfs as i_dfs
from a_star import a_star_h1
import helpers

puzzle_length = 4
number_of_puzzles = 30
puzzle = Puzzle(puzzle_length)
puzzles = {10: [], 15: [], 20: [], 25: []}

#disorders the puzzle
for key in puzzles:
    
    for i in range(number_of_puzzles):
        puzzles[key].append(helpers.disorder_puzzle(key, puzzle))
node = helpers.disorder_puzzle(10,puzzle)
print(a_star_h1(helpers.deepcopy(node)))
print(i_dfs(helpers.deepcopy(node)))
'''
# assigns the same disorded puzzles to the lists to be ran for the respective algorithm
idfs_puzzles = helpers.deepcopy(puzzles)
h1_puzzles = helpers.deepcopy(puzzles)
h2_puzzles = helpers.deepcopy(puzzles)

# gets the results
# as the IDFS algorithm is too slow, it won't calculate for 25 moves puzzles
idfs_puzzles.pop(25)
idfs_results = helpers.run_algorithm(idfs_puzzles, i_dfs)
h1_results = []
h2_results = []

#computes results
idfs_means = dict()
idfs_medians = dict()
idfs_std_devs_mean = dict()
idfs_std_devs_median = dict()

for key in idfs_results:
    
    idfs_means[key] = helpers.mean(idfs_results[key])
    idfs_medians[key] = helpers.median(idfs_results[key])
    idfs_std_devs_mean[key] = helpers.stdev(idfs_results[key], idfs_means[key])
    idfs_std_devs_median[key] = helpers.stdev(idfs_results[key], idfs_medians[key])

print(' mean :' + str(idfs_means[10]) +
      '\n median:' + str(idfs_medians[10]) +
      '\n std dev mean:' + str(idfs_std_devs_mean[10]) +
      '\n std dev median:' + str(idfs_std_devs_median[10]))
'''