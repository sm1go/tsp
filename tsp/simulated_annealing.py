import math
import random
from tsp.utils import tour_length, euclidean

def simulated_annealing(points, initial_tour, initial_temp=2000, cooling_rate=0.995, min_temp=0.001):
    current_tour = initial_tour[:]
    best_tour = initial_tour[:]
    
    current_len = tour_length(points, current_tour)
    best_len = current_len
    
    temp = initial_temp
    n = len(points)
    
    epoch_length = int(n) 
    if epoch_length < 10: epoch_length = 10

    while temp > min_temp:
        for _ in range(epoch_length):
            i = random.randint(0, n - 2)
            j = random.randint(i + 1, n - 1)
            
            if i == 0 and j == n - 1:
                continue
            
            p1, p2 = points[current_tour[i]], points[current_tour[i+1]]
            p3, p4 = points[current_tour[j]], points[current_tour[(j+1) % n]]
            
            loss_old = euclidean(p1, p2) + euclidean(p3, p4)
            loss_new = euclidean(p1, p3) + euclidean(p2, p4)
            delta = loss_new - loss_old
            
            if delta < 0 or random.random() < math.exp(-delta / temp):
                current_tour[i+1 : j+1] = reversed(current_tour[i+1 : j+1])
                current_len += delta
                
                if current_len < best_len:
                    best_tour = current_tour[:]
                    best_len = current_len

        temp *= cooling_rate
        
    return best_tour