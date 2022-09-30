import csv
def learn_prior(file_name, pseudo_count=0):
    """
        Takes the file name of the training set and an optional pseudo-count 
        parameter and returns a real number that is the prior probability of 
        spam being true. The parameter pseudo_count is a non-negative integer 
        and it will be the same for all the attributes and all the values.
    """

    with open(file_name) as in_file:
            training_examples = [tuple(row) for row in csv.reader(in_file)] 

    trues = 0
    for row in training_examples[1:]:
        trues += int(row[12])
    return (trues + pseudo_count)/((len(training_examples) - 1)+(pseudo_count * 2))

def learn_likelihood(file_name, pseudo_count=0):
    """
        Takes the file name of a training set (for the spam detection problem) 
        and an optional pseudo-count parameter and returns a sequence of pairs 
        of likelihood probabilities. As described in the representation of 
        likelihood, the length of the returned sequence (list or tuple) must be 
        12. Each element in the sequence is a pair (tuple) of real numbers such 
        that likelihood[i][False] is P(X[i]=true|Spam=false) and likelihood[i][True] 
        is P(X[i]=true|Spam=true ).
    """

    with open(file_name) as in_file:
            training_examples = [tuple(row) for row in csv.reader(in_file)] 
    
    
    variables = training_examples[0][:-1]
    results = []
    for i in range(len(variables)):
        numSpamTrue = 0
        numSpamFalse = 0
        numTrueGivenSpamTrue = 0
        numTrueGivenSpamFalse = 0
        for row in training_examples[1:]:
            if row[12] == '1':
                numTrueGivenSpamTrue += int(row[i])
                numSpamTrue += 1
            else:
                numTrueGivenSpamFalse += int(row[i])
                numSpamFalse += 1
        pGivenTrue = (numTrueGivenSpamTrue + pseudo_count)/(numSpamTrue + (pseudo_count * 2))
        pGivenFalse = (numTrueGivenSpamFalse + pseudo_count)/(numSpamFalse + (pseudo_count * 2))
        results.append((pGivenFalse, pGivenTrue))
    return results

def posterior(prior, likelihood, observation):
    """
        Returns the posterior probability of the class variable being true, 
        given the observation; that is, it returns p(Class=true|observation). 
        The argument observation is a tuple of n Booleans such that 
        observation[i] is the observed value (True or False) for the 
        input feature X[i].
    """
    true = prior 
    false = 1 - prior
    
    for i in range(len(observation)):

        true *= likelihood[i][True] if observation[i] else (1-likelihood[i][True]) # P(X | class=True)
        false *= likelihood[i][False] if observation[i] else (1-likelihood[i][False]) # P(X | class=False)
    
    return true / (true + false)

def nb_classify(prior, likelihood, input_vector):
    """
        Takes the learnt prior and likelihood probabilities and classifies 
        an (unseen) input vector. The input vector will be a tuple of 12 
        integers (each 0 or 1) corresponding to attributes X1 to X12. The 
        function should return a pair (tuple) where the first element is 
        either "Spam" or "Not Spam" and the second element is the certainty. 
        The certainty is the (posterior) probability of spam when the instance 
        is classified as spam, or the probability of 'not-spam' otherwise. If 
        spam and 'not spam' are equally likely (i.e. p=0.5) then choose 'not spam'.
    """

    pSpam = posterior(prior, likelihood, input_vector)
    if pSpam <= 0.5:
        return 'Not Spam', 1 - pSpam
    else:
        return 'Spam', pSpam

if __name__ == '__main__':
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
            .format(label, certainty))
    print()

    
    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
            .format(label, certainty))