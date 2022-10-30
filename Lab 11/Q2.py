def min_value(tree):
    if type(tree) == int:
        return tree
    else:
        min = float('inf')
        for val in tree:
            res = max_value(val)
            if res < min:
                min = res
        return min

def max_value(tree):
    if type(tree) == int:
        return tree
    else:
        min = float('inf') * -1
        for val in tree:
            res = min_value(val)
            if res > min:
                min = res
        return min

def max_action_value(game_tree):
    if type(game_tree) == int:
        return (None, game_tree)
    else:
        max_index = -1
        max_value_number = float("inf") * -1
        for i in range(len(game_tree)):
            res = min_value(game_tree[i])
            if res > max_value_number:
                max_value_number = res
                max_index = i
        return (max_index, max_value_number)

def min_action_value(game_tree):
    if type(game_tree) == int:
        return (None, game_tree)
    else:
        min_index = -1
        min_value_number = float("inf")
        for i in range(len(game_tree)):
            res = max_value(game_tree[i])
            if res < min_value_number:
                min_value_number = res
                min_index = i
        return (min_index, min_value_number)

if __name__ == "__main__":
    game_tree = [2, [-3, 1], 4, 1]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)