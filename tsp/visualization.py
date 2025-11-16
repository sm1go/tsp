import matplotlib.pyplot as plt
from typing import List
from .utils import Point

def plot_tour(points: List[Point], tour: List[int], title: str = "TSP Tour"):
    xs = [points[i][0] for i in tour + [tour[0]]]
    ys = [points[i][1] for i in tour + [tour[0]]]

    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, '-o')
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
