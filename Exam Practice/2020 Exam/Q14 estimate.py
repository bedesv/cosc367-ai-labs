
def estimate(time, observations, k):
    # print()
    # print(time)
    # observations.sort(key=lambda x: x[0], reverse = True)
    # print(observations)
    observations.sort(key=lambda x: abs(time - x[0]))
    # print(observations)
    while k < len(observations) and abs(time - observations[k-1][0]) == abs(time - observations[k][0]):
        k += 1
    if k > len(observations):
        k = len(observations)
    total = 0
    for observation in observations[:k]:
        total += observation[1]
    return total / k

if __name__ == "__main__":
    observations = [
        (-1, 1),
        (0, 0),
        (-1, 1),
        (5, 6),
        (2, 0),
        (2, 3),
    ]

    for time in [-1, 1, 3, 3.5, 6]:
        print(estimate(time, observations, 2))