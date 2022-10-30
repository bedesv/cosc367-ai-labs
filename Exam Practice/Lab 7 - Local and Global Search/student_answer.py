def n_queens_neighbours(state):
    neighbours = set()
    for i in range(len(state)):
        for j in range(len(state)):
            if j != i:
                temp = list(state)
                temp[j], temp[i] = temp[i], temp[j]
                neighbours.add(tuple(temp))
    return sorted(list(neighbours))

def n_queens_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            dx = i - j
            dy = state[i] - state[j]
            if abs(dx) == abs(dy):
                cost += 1
    return cost

def greedy_descent(initial_state, neighbours, cost):
    current_state = initial_state
    visited_states = [current_state]
    
    while neighbours(current_state)!= []:
        next_states = neighbours(current_state)
        next_states.sort(key=lambda x: cost(x))

        if cost(next_states[0]) < cost(current_state):
            current_state = next_states[0]
            visited_states.append(current_state)
        else:
            break
    return visited_states

def greedy_descent_with_random_restart(random_state, neighbours, cost):
    
    state = random_state()
    visited = greedy_descent(state, neighbours, cost)
    [print(x) for x in visited]
    while cost(visited[-1]) != 0:
        print("RESTART")
        state = random_state()
        visited = greedy_descent(state, neighbours, cost)
        [print(x) for x in visited]