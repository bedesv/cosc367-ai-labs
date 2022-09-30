import csv

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

likelihood = learn_likelihood("spam-labelled.csv")
print(len(likelihood))
print([len(item) for item in likelihood])

likelihood = learn_likelihood("spam-labelled.csv")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))