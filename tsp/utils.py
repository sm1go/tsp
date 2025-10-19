import math 
from typing import List, Tuple 

Point = Tuple[float, float]

def euclidean(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def tour_length(points: List[Point], tour: List[int]) -> float:
    total = 0.0 
    for i in range(len(tour)):
        total += euclidean(points[tour[i]], points[tour[(i + 1) % len(tour)]])
    return total
