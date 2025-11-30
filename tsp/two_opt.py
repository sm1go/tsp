from tsp.utils import euclidean

def two_opt(points, tour):
    best_tour = tour[:]
    improved = True
    n = len(points)
    
    while improved:
        improved = False
        for i in range(n - 1):
            for j in range(i + 2, n):
                if j == n - 1 and i == 0: 
                    continue 
                
                p1, p2 = points[best_tour[i]], points[best_tour[i+1]]
                p3, p4 = points[best_tour[j]], points[best_tour[(j+1) % n]]
                
                current_dist = euclidean(p1, p2) + euclidean(p3, p4)
                new_dist = euclidean(p1, p3) + euclidean(p2, p4)
                
                if new_dist < current_dist:
                    best_tour[i+1 : j+1] = reversed(best_tour[i+1 : j+1])
                    improved = True
                    break 
            if improved:
                break
                
    return best_tour