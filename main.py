from tsp.generator import generate_unique_points, write_instance, read_instance
from tsp.greedy import nearest_neighbor
from tsp.utils import tour_length

def main():
    n = 100
    path = "data/instances/tsp_100.txt"

    cities = generate_unique_points(n, x_max=2000, y_max=2300, seed=42)
    write_instance(cities, path)

    points = read_instance(path)

    tour = nearest_neighbor(points)
    length = tour_length(points, tour)

    print("\n TSP (Nearest Neighbor):")
    print("Tour:", " -> ".join(str(i + 1) for i in tour))
    print(f"Tour length: {length:.2f}")

if __name__ == "__main__":
    main()
