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


if __name__ == "__main__":
    game_tree = [1, 2, [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))