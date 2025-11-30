import argparse
import os
from tsp.generator import generate_unique_points, write_instance

def main():
    parser = argparse.ArgumentParser(description="Generator instancji TSP")
    parser.add_argument("n", type=int, help="Liczba miast do wygenerowania")
    parser.add_argument("--filename", type=str, default=None, help="Nazwa pliku wyjściowego")
    
    args = parser.parse_args()
    
    if args.filename is None:
        filename = f"data/instances/tsp_{args.n}.txt"
    else:
        filename = args.filename
        
    print(f"Generowanie {args.n} miast...")
    cities = generate_unique_points(n=args.n, seed=None)
    
    write_instance(cities, filename)

if __name__ == "__main__":
    main()