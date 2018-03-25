"""
This file contains utilities and other basic tools used in the homework exercise.

It contains code related to loading a TSP problem, and some initial simple implementations.
"""
import random

def initial_value_random(n, dist):
    """
    Generate an random initial value for a TSP problem with n places and an distance matrix dist.
    
    Note that the distance matrix dist is ignored as the value is random.
    """
    return random.shuffle(list(range(n)))

def load_tsp_problem():
    """
    Loads the TSP problem for this assignment as a distance matrix.
    """
    raise NotImplementedError
