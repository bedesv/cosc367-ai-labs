from itertools import product

def joint_prob(network, assignment):
    probability = 1
    for i in assignment.keys():
        key = []
        for parent in network[i]["Parents"]:
            key.append(assignment[parent])
        prob = network[i]["CPT"][tuple(key)]
        probability *= prob if assignment[i] else (1 - prob)
    return probability

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Find the hidden variables
    # Initialise a raw distribution to [0, 0]
    result = [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            # Update the assignment (we now have a complete assignment)
            assignment = assignment | hidden_assignments
            result[query_value] += joint_prob(network, assignment)
            # Update the raw distribution by the probability of the assignment.
    # Normalise the raw distribution and return it
    result = {True: result[1] / sum(result), False: result[0] / sum(result)}
    return result

network = {

    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01
            }},
    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.1,
            }},
            
    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},
    
    }

answer = query(network, 'Virus', {'A': True})
print("The probability of carrying the virus\n"
      "if test A is positive: {:.5f}"
      .format(answer[True]))