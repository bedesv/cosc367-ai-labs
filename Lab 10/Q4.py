def accuracy(classifier, inputs, expected_outputs):
    """
        passes each input in the sequence of inputs to the given classifier 
        function (e.g. a perceptron) and compares the predictions with the 
        expected outputs. The function returns the accuracy of the 
        classifier on the given data. Accuracy must be a number between 0 
        and 1 (inclusive).
    """
    results = []
    for i in range(len(inputs)):
        results.append(1 if classifier(inputs[i]) == expected_outputs[i] else 0)
    return sum(results) / len(results)

if __name__ == "__main__":
    from Q3 import construct_perceptron
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]

    print(accuracy(perceptron, inputs, targets))