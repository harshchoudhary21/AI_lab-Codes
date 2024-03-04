import random
import math

# Define the TSP objective
def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i-1]][tour[i]] for i in range(len(tour)))

# Generate a new tour by swapping two cities
def generate_tour(current_tour):
    new_tour = current_tour[:]
    i, j = random.sample(range(len(new_tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

# Simulated Annealing algorithm
def simulated_annealing(cities, distance_matrix, initial_temperature, cooling_rate, num_iterations):
    current_tour = random.sample(cities, len(cities))  # Start with a random tour
    current_distance = total_distance(current_tour, distance_matrix)

    for i in range(num_iterations):
        temperature = initial_temperature * (cooling_rate ** i)
        new_tour = generate_tour(current_tour)
        new_distance = total_distance(new_tour, distance_matrix)
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour, current_distance = new_tour, new_distance

    return current_tour, current_distance

# Define cities and distance matrix
cities = ['A', 'B', 'C', 'D', 'E']
distance_matrix = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'E': 10},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25, 'E': 15},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30, 'E': 20},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0, 'E': 15},
    'E': {'A': 10, 'B': 15, 'C': 20, 'D': 15, 'E': 0},
}

# Run the algorithm
initial_temperature = 1000
cooling_rate = 0.995
num_iterations = 10000
best_tour, best_distance = simulated_annealing(cities, distance_matrix, initial_temperature, cooling_rate, num_iterations)

print(f"Best tour: {best_tour}")
print(f"Best distance: {best_distance}")