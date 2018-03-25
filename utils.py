"""
This file contains utilities and other basic tools used in the homework exercise.

It contains code related to loading a TSP problem, and some initial simple implementations.
"""
import random
import math

def random_initial_value(n, dist):
    """
    Generate an random initial value for a TSP problem with n places and an distance matrix dist.
    
    Note that the distance matrix dist is ignored as the value is random.
    """
    initial = list(range(n))
    random.shuffle(initial)
    return initial

def objective_tsp(sequence, dist):
    """
    Calculate the objective value for a tour defined by this sequence.
    
    The last element connects back to the first element.
    """
    return sum(dist[i][j] for (i, j) in zip(sequence, sequence[1:])) + \
        dist[sequence[len(sequence)-1]][ sequence[0]] 

def load_tsp_problem():
    """
    Loads the TSP problem for this assignment.
    
    Returns (n, dist)
    """
    raise NotImplementedError
    
def distance(p, q):
    """
    Calculate the distance between two points p and q.
    """
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

def generate_euclid_tsp_problem(n, lower, upper):
    """
    Generate an TSP problem with Euclidian distances.
    
    Returns (n, dist)
    """
    # Create n x n matrix.
    dist = [[0 for _ in range(n)] for _ in range(n)]
    # Generate n random 2D points.
    points = [(random.uniform(lower, upper), random.uniform(lower, upper)) for _ in range(n)]
    # Update distance matrix.
    for p in range(n):
        for q in range(p + 1, n):
            d = distance(points[p], points[q])
            dist[p][q] = d
            dist[q][p] = d
    return n, dist