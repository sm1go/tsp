from tsp.two_opt import two_opt
from tsp.greedy import nearest_neighbor
from tsp.generator import read_instance
from tsp.utils import tour_length
from experiments.run_experiments import run_experiment

def main():
    path = "data/instances/tsp_52.txt"
    points = read_instance(path)
    print(f"Wczytano {len(points)} punktów z pliku: {path}")

    tour = nearest_neighbor(points)
    n = len(points)
    if set(tour) != set(range(n)) or len(tour) != n:
        raise ValueError("Tour nie jest poprawną permutacją indeksów miast.")

    tour_with_return = tour + [tour[0]]
    print("\nTSP (Nearest Neighbor):")
    print("Tour:", " -> ".join(str(i + 1) for i in tour_with_return))

    length = tour_length(points, tour)
    print(f"Tour length: {length:.2f}")

    run_experiment(path, use_two_opt=True)

if __name__ == "__main__":
    main()
