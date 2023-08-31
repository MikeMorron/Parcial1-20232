
#---------------Examen Por Michael Morron---------------------------

#en el ejercicio no nos dieron valores fijos asi que use valores aleatorios...

import random
import math

# le digo al programa que quiero distancias aleatorias
def generate_random_points(num_points, min_val, max_val):
    points = []
    for _ in range(num_points):
        x = random.randint(min_val, max_val)
        y = random.randint(min_val, max_val)
        points.append((x, y))
    return points

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest_pair(points):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

# divide y venceras :V (nombre raro para una funcion)
def divide_and_conquer_closest_pair(points):
    if len(points) <= 3:
        return brute_force_closest_pair(points)

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    left_pair, left_distance = divide_and_conquer_closest_pair(left_points)
    right_pair, right_distance = divide_and_conquer_closest_pair(right_points)

    min_distance = min(left_distance, right_distance)
    min_pair = left_pair if left_distance < right_distance else right_pair

    strip_points = [point for point in points if abs(point[0] - points[mid][0]) < min_distance]
    strip_points.sort(key=lambda x: x[1])

    for i in range(len(strip_points)):
        j = i + 1
        while j < len(strip_points) and strip_points[j][1] - strip_points[i][1] < min_distance:
            dist = distance(strip_points[i], strip_points[j])
            if dist < min_distance:
                min_distance = dist
                min_pair = (strip_points[i], strip_points[j])
            j += 1

    return min_pair, min_distance

# aplicamos los args y kwargs
def measure_time(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# aqui esta la funcion de pares cercanos
def pares_cercanos(points):
    sorted_points = sorted(points, key=lambda x: x[0])
    closest_pair, distance = divide_and_conquer_closest_pair(sorted_points)
    return closest_pair, distance

# Generamos puntos aleatorios en cada ejecución
random.seed()  
num_points = 10
min_val, max_val = 0, 20
points = generate_random_points(num_points, min_val, max_val)

# Mostramos los resultados
closest_pair, distance = pares_cercanos(points)
print("===================================================")
print(" || Puntos más cercanos:", closest_pair)
print(" || Distancia entre ellos:", distance)
print("===================================================")
