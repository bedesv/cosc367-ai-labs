

def knn_predict(input, examples, distance, combine, k):
    """
        Takes an input and predicts the output by combining the output of the k nearest neighbours. 
        If after selecting k nearest neighbours, the distance to the farthest selected neighbour 
        and the distance to the nearest unselected neighbour are the same, more neighbours must 
        be selected until these two distances become different or all the examples are selected. 
        The description of the parameters of the function are as the following:

        input:    an input object whose output must be predicted. Do not make any assumption about the type of 
                  input other than that it can be consumed by the distance function.
        examples: a collection of pairs. In each pair the first element is of type input and the second 
                  element is of type output.
        distance: a function that takes two objects and returns a non-negative number that is the distance 
                  between the two objects according to some metric.
        combine:  a function that takes a set of outputs and combines them in order to derive a new prediction (output).
        k:        a positive integer which is the number of nearest neighbours to be selected. If there is a tie more 
                  neighbours will be selected (see the description above).
    """
    examples.sort(key=lambda x: distance(input, x[0]))

    while k < len(examples) and distance(input, examples[k-1][0]) == distance(input, examples[k][0]):
        k += 1
        
    return combine([x[1] for x in examples[:k]])





if __name__ == "__main__":
    from Q1 import euclidean_distance, majority_element
    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]

    distance = euclidean_distance
    combine = majority_element

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()

    print()
    print()

    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]

    def average(values):
        return sum(values) / len(values)

    distance = euclidean_distance
    combine = average

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()