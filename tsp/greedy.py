from typing import List, Tuple
from tsp.utils import euclidean, tour_length

Point = Tuple[float, float]

def nearest_neighbor(points: List[Point]) -> List[int]:
    """Zachłanny algorytm TSP (Nearest Neighbor)."""
    n = len(points)
    unvisited = set(range(n))
    tour = [0]  # start z miasta 0
    unvisited.remove(0)
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda j: euclidean(points[current], points[j]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    return tour
