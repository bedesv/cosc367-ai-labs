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



prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true)) 