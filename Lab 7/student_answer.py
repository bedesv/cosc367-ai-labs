def n_queens_neighbours(state):
    """
        Takes a state (total assignment) for an n-queen problem and returns a sorted list of states that are the
        neighbours of the current assignment. A neighbour is obtained by swapping the position of two numbers in
        the given permutation.
    """
    result = set()
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                state_copy = list(state)
                state_copy[i], state_copy[j] = state_copy[j], state_copy[i]
                result.add(tuple(state_copy))
    return sorted(result)


def n_queens_cost(state):
    """
        Takes a state (a total assignment) for an n-queen problem and returns the number conflicts for that state.
        We define the number of conflicts to be the number of unordered pairs of queens (objects) that threaten (attack)
        each other. The state will be given in the form of a sequence (tuple more specifically). The state is a
        permutation of numbers from 1 to n (inclusive). The value of n must be inferred from the given state.
    """

    conflicts = 0
    checked = set()
    n = len(state)
    for i in range(n):
        for j in range(n):
            if i != j and (i, j) not in checked and (j, i) not in checked:
                dx = abs(i - j)
                dy = abs(state[i]-state[j])
                if dx == dy:
                    checked.add((i, j))
                    conflicts += 1
    return conflicts


def greedy_descent(initial_state, neighbours, cost):
    """
        Takes an initial state and two functions to compute the neighbours and cost of a state, and then iteratively
        improves the state until a local minimum (which may be global) is reached. The function must return the list of
        states it goes through (including the first and last one) in the order they are encountered. The algorithm
        should move to a new state only if the cost improves. If there is a tie between multiple states, the first one
        (in the order they appear in the sequence returned by neighbours) must be used.
    """
    states_visited = [initial_state]
    curr_cost = cost(initial_state)
    curr_state = initial_state

    while True:
        neighbour_options = neighbours(curr_state)
        if len(neighbour_options) == 0:
            break
        min_neighbour = min(neighbour_options, key=lambda x: cost(x))
        if cost(min_neighbour) < curr_cost:
            curr_cost = cost(min_neighbour)
            states_visited.append(min_neighbour)
            curr_state = min_neighbour
        else:
            break
    return states_visited


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    """
        Takes three functions, one to get a new random state and two to compute the neighbours or cost of a state and
        then uses greedy_descent (you wrote earlier) to find a solution. The first state in the search must be obtained
        by calling the function random_state. The procedure must print each state it goes through (including the first
        and last one) in the order they are encountered. When the search reaches a local minimum that is not global,
        the procedure must print RESTART and restart the search by calling random_state.
    """
    initial_state = random_state()
    states = greedy_descent(initial_state, neighbours, cost)
    [print(x) for x in states]

    while cost(states[-1]) != 0:
        print("RESTART")
        initial_state = random_state()
        states = greedy_descent(initial_state, neighbours, cost)
        [print(x) for x in states]


def roulette_wheel_select(population, fitness, r):
    """
        Takes a list of individuals, a fitness function, and a floating-point random number r in the interval [0, 1),
        and selects and returns an individual from the population using the roulette wheel selection mechanism. The
        fitness function (which will be provided as an argument) takes an individual and returns a non-negative number
        as its fitness. The higher the fitness the better. When constructing the roulette wheel, do not change the order
        of individuals in the population.
    """
    t = 0
    for individual in population:
        t += fitness(individual)
    n = t * r

    running_total = 0
    for individual in population:
        running_total += fitness(individual)
        if running_total >= n:
            return individual

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))