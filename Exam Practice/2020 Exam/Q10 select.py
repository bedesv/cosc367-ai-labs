def select(population, error, max_error, r):

    fitness_sum = 0
    for i in population:
        fitness_sum += (max_error - error(i))

    target = fitness_sum * r
    fitness_sum = 0
    for individual in population:
        fitness_sum += (max_error - error(individual))
        if fitness_sum > target:
            return individual


if __name__ == "__main__":
    population = ['a', 'b']

    def error(x):
        return {'a': 14,
                'b': 12}[x]

    max_error = 15

    for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
        print(select(population, error, max_error, r))

    # since the fitness of 'a' is 1 and the fitness of 'b' is 3,
    # for r's below 0.25 we get 'a', for r's above it we get 'b'.