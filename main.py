import random

# cities as (x, y) coordinates
cities = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# initial population of routes
def create_population(num_routes, cities):
    population = []
    for _ in range(num_routes):
        route = random.sample(cities, len(cities))
        population.append(route)
    return population

# Calculate the total distance of route
def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        x1, y1 = route[i]
        x2, y2 = route[i + 1]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        total_distance += distance
    return total_distance

# Select parents for reproduction
def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        tournament = random.sample(population, 3)
        best_route = min(tournament, key=calculate_distance)
        parents.append(best_route)
    return parents

# Perform crossover to create new routes partially mapped crossove
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child = [None] * len(parent1)
    for i in range(start, end):
        child[i] = parent1[i]
    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(child)):
                if child[j] is None:
                    child[j] = parent2[i]
                    break
    return child

#mutation
def mutate(route):
    index1, index2 = random.sample(range(len(route)), 2)
    route[index1], route[index2] = route[index2], route[index1]

# Genetic Algorithm parameters
population_size = 50
num_generations = 100

#initial population
population = create_population(population_size, cities)

# Main genetic algorithm loop
for generation in range(num_generations):
    parents = select_parents(population, population_size // 2)
    
    # Create new generation
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        if random.random() < 0.1:
            mutate(child)
        new_population.append(child)
    
    # Replace old population with new population
    population = new_population

# Find the best route in the final population
best_route = min(population, key=calculate_distance)
print("Best Route:", best_route)
print("Total Distance:", calculate_distance(best_route))
