import random

def fitness(chromosome):
    return sum(chromosome)

def selection(population):
    population.sort(key=fitness, reverse=True)
    return population[:2]

def crossover(parent1, parent2):
    point = random.randint(1, 4)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutation(chromosome):
    chromosome = chromosome[:]
    index = random.randint(0, 4)
    chromosome[index] = 1 - chromosome[index]
    return chromosome

# Initial population of 6 chromosomes, each 5 bits long
population = [
    [random.randint(0, 1) for _ in range(5)]
    for _ in range(6)
]

# Run for 5 generations
for generation in range(1, 6):
    print("\nGeneration", generation)
    
    for chromosome in population:
        print("".join(map(str, chromosome)), "Fitness:", fitness(chromosome))
        
    parents = selection(population)
    new_population = parents[:]
    
    while len(new_population) < 6:
        child1, child2 = crossover(parents[0], parents[1])
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_population.append(child1)
        if len(new_population) < 6:
            new_population.append(child2)
            
    population = new_population

best = max(population, key=fitness)
print("\nBest Solution:")
print("".join(map(str, best)))
print("Fitness:", fitness(best))