import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # dodaje tsp_project
from tsp.utils import tour_length

def two_opt(points, tour):
    improved = True
    best = tour
    best_distance = tour_length(points, best)

    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1:
                    continue
                new_tour = best[:]
                new_tour[i:j] = reversed(new_tour[i:j])
                new_distance = tour_length(points, new_tour)
                if new_distance < best_distance:
                    best = new_tour
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break
    return best
