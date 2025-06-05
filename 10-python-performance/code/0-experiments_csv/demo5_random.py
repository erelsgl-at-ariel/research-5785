"""
Demo 5: demonstrates running experiments on random inputs, and averaging the results.
"""
import numpy as np

def adder(x, y, z):
    return {"sum": x+y+z}

def adder_random_input(x,y,z,seed):
    np.random.seed(seed)
    x = x ** np.random.random()
    return adder(x,y,z)

import experiments_csv, logging
ex = experiments_csv.Experiment("results/", "demo5.csv", backup_folder="results/backups")
ex.clear_previous_results()

input_ranges = {
    "x": range(20),
    "y": [5,10,15],
    "z": [15,20,25],
    "seed": range(10)
}
ex.run_with_time_limit(adder_random_input, input_ranges, time_limit=5)
