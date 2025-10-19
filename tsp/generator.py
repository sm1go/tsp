import random
from typing import List, Tuple
import os

City = Tuple[int, float, float]


def generate_unique_points(n: int, x_max: int = 2000, y_max: int = 2000, seed: int = None) -> List[City]:
    if seed is not None:
        random.seed(seed)

    points = set()
    while len(points) < n:
        x = random.randint(0, x_max)
        y = random.randint(0, y_max)
        points.add((x, y))

    return [(i + 1, float(x), float(y)) for i, (x, y) in enumerate(points)]


def write_instance(cities: List[City], filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(f"{len(cities)}\n")
        for cid, x, y in cities:
            f.write(f"{cid} {int(x)} {int(y)}\n")
    print(f"Instance saved: {filename}")


def read_instance(filename: str) -> List[Tuple[float, float]]:
    with open(filename, "r") as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    points = []
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) == 3:
            _, x, y = parts
            points.append((float(x), float(y)))

    if len(points) != n:
        raise ValueError("Error: Number of points does not match.")

    return points
