def roulette_wheel_select(population, fitness, r):

    total_fitness = 0
    for i in population:
        total_fitness += fitness(i)
    target_fitness = total_fitness * r

    fitness_sum = 0
    for i in population:
        fitness_sum += fitness(i)
        if fitness_sum > target_fitness:
            return i

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))