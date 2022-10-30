def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    """
        Adjusts the weights and bias by iterating through the training data and applying the perceptron 
        learning rule. The function must return a pair (2-tuple) where the first element is the vector 
        (list) of adjusted weights and second argument is the adjusted bias. 
        
        The parameters of the function are:

        weights:           an array (list) of initial weights of length n
        bias:              a scalar number which is the initial bias
        training_examples: a list of training examples where each example is a pair. The first element 
                           of the pair is a vector (tuple) of length n. The second element of the pair 
                           is an integer which is either 0 or 1 representing the negative or positive 
                           class correspondingly.
        learning_rate:     a positive number representing eta in the learning equations of perceptron.
        max_epochs:        the maximum number of times the learner is allowed to iterate through all the 
                           training examples.
    """

    for _ in range(max_epochs):
        failed = False
        for example in training_examples:
            inputs = example[0]
            target = example[1]
            output = bias
            for i in range(len(weights)):
                output += weights[i] * inputs[i]
            output = 1 if output >= 0 else 0
            if output != target:
                failed = True
                for i in range(len(weights)):
                    new_weight = weights[i] + learning_rate * inputs[i] * (target - output)
                    weights[i] = new_weight
                bias = bias + learning_rate * (target - output)
        
        if not failed:
            break
    return (weights, bias)
            


if __name__ == "__main__":
    from Q3 import construct_perceptron
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 1),
    ((1, 1), 0),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")