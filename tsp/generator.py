import csv 
import random 
from typing import List, Tuple 

City = Tuple[int, float, float]

def generate_unique_points(n: int, x_max: int = 1000, y_max: int = 1000, seed: int = None) -> List[City]:
    if seed is not None:
        random.seed(seed)
    if n > x_max * y_max:
        raise ValueError("Too many points for a specific range.")
    all_indices = list(range(x_max * y_max))
    chosen = random.sample(all_indices, n)
    pts = [(i, idx % x_max, idx // x_max) for i, idx in enumerate(chosen)]
    return [(i, float(x), float(y)) for i, x, y in pts]

def write_instance(cities: List[City], filename: str):
    with open(filename, 'w', newline='') as f: 
        writer = csv.writer(f)
        writer.writerow(['id', 'x', 'y'])
        for cid, x, y in cities:
            writer.writerow([cid, f"{x:.3f}", f"{y:.3f}"])


def read_instance(filename: str) -> List[Tuple[float, float]]:
    points = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader: 
            points.append((float(row['x']), float(row['y'])))
        return points


