import argparse
import time
import csv
import os
import random
from datetime import datetime
from tsp.greedy import nearest_neighbor
from tsp.two_opt import two_opt
from tsp.simulated_annealing import simulated_annealing
from tsp.generator import read_instance
from tsp.utils import tour_length

def save_result_to_csv(filename, instance_name, method, score, time_elapsed, params=""):
    os.makedirs("results", exist_ok=True)
    filepath = os.path.join("results", filename)
    file_exists = os.path.isfile(filepath)
    
    with open(filepath, mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        if not file_exists:
            writer.writerow(["Data", "Instancja", "Metoda", "Dlugosc_Trasy", "Czas_s", "Parametry"])
            
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            instance_name,
            method,
            f"{score:.2f}",
            f"{time_elapsed:.4f}",
            params
        ])

def main():
    parser = argparse.ArgumentParser(description="TSP Solver Experiment")
    parser.add_argument("--temp", type=float, default=2000.0, help="Temperatura początkowa SA")
    parser.add_argument("--rate", type=float, default=0.9995, help="Współczynnik schładzania SA")
    parser.add_argument("--file", type=str, default="data/instances/tsp_52.txt", help="Ścieżka do instancji")
    parser.add_argument("--random", action="store_true", help="Startuj SA z losowej permutacji (zamiast NN)")
    args = parser.parse_args()

    try:
        points = read_instance(args.file)
    except FileNotFoundError:
        print(f"Błąd: Plik '{args.file}' nie istnieje.")
        return

    instance_name = os.path.basename(args.file)
    print(f"--- EKSPERYMENT: {instance_name} (Liczba miast: {len(points)}) ---")

    # --- 1. Nearest Neighbor ---
    start = time.time()
    tour_nn = nearest_neighbor(points)
    time_nn = time.time() - start
    len_nn = tour_length(points, tour_nn)
    
    print(f"NN (Greedy):      {len_nn:.2f}")
    save_result_to_csv("eksperymenty.csv", instance_name, "Nearest Neighbor", len_nn, time_nn)

    # --- 2. 2-opt (Local Search) ---
    start = time.time()
    tour_2opt = two_opt(points, tour_nn)
    time_2opt = time.time() - start
    len_2opt = tour_length(points, tour_2opt)
    
    print(f"2-opt:            {len_2opt:.2f}")
    save_result_to_csv("eksperymenty.csv", instance_name, "2-opt", len_2opt, time_2opt)

    # --- 3. Simulated Annealing (Rozdzielone wyniki) ---
    start_mode = "RANDOM" if args.random else "NN"
    print(f"\n--- Uruchamianie SA (Start: {start_mode}) ---")
    
    # A. Przygotowanie trasy startowej
    if args.random:
        tour_start = list(range(len(points)))
        random.shuffle(tour_start)
    else:
        tour_start = tour_nn[:]

    # B. Uruchomienie "Czystego" SA
    start_sa = time.time()
    tour_sa_raw = simulated_annealing(
        points, 
        tour_start, 
        initial_temp=args.temp, 
        cooling_rate=args.rate
    )
    time_sa_raw = time.time() - start_sa
    len_sa_raw = tour_length(points, tour_sa_raw)
    
    print(f"SA (Raw):         {len_sa_raw:.2f} (Czas: {time_sa_raw:.4f}s)")
    
    params_raw = f"T={args.temp}, rate={args.rate}, start={start_mode}"
    save_result_to_csv("eksperymenty.csv", instance_name, "Simulated Annealing (Raw)", len_sa_raw, time_sa_raw, params_raw)

    # C. Hybrydyzacja (Poprawianie wyniku SA algorytmem 2-opt)
    start_hybrid = time.time()
    tour_sa_hybrid = two_opt(points, tour_sa_raw)
    time_hybrid_total = (time.time() - start_hybrid) + time_sa_raw # Czas sumaryczny (SA + 2opt)
    len_sa_hybrid = tour_length(points, tour_sa_hybrid)

    print(f"SA + Hybrid:      {len_sa_hybrid:.2f}")
    
    save_result_to_csv("eksperymenty.csv", instance_name, "SA + 2-opt Hybrid", len_sa_hybrid, time_hybrid_total, params_raw)

    print("\nWyniki zapisane do: results/eksperymenty.csv")

if __name__ == "__main__":
    main()