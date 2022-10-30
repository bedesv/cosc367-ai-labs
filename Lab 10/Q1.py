from math import sqrt
def euclidean_distance(v1, v2):
    """
        v1 and v2 are two numeric vectors (non-empty sequences) with the same 
        number of elements. The function returns the Euclidean distance 
        between the points represented by v1 and v2.
    """
    total = 0
    for i in range(len(v1)):
        total += (v1[i] - v2[i])**2
    return sqrt(total)

def majority_element(labels):
    """
        labels is a non-empty collection of class labels. The function returns 
        a label that has the highest frequency (most common). 
        [if there is a tie it doesn't matter which majority is returned.] 
        This is an example of a combine function.
    """
    frequencies = {}
    for label in labels:
        if label in frequencies:
            frequencies[label] += 1
        else:
            frequencies[label] = 1
    max_val = [keys for keys,values in frequencies.items() if values == max(frequencies.values())]
    return min(max_val)


if __name__ == "__main__":
    print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
    print(majority_element([1, 0, 0, 0, 1, 1, -1, -1, -1]))
    print(majority_element("ababc") in "ab")