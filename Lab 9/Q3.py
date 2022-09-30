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

prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))
prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))
prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))
prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))
prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))
prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))
prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))