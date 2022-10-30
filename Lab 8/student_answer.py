from itertools import product
def joint_prob(network, assignment):
    """
        Takes a belief network and a complete assignment of all the variables in the 
        network, and returns the probability of the assignment. The data structure 
        of the network is as described above. The assignment is a dictionary where 
        keys are the variable names and the values are either True or False.
    """
    p = 1
    for var in network:
        parents_requirement = tuple([assignment[parent] for parent in network[var]['Parents']])
        p *= (network[var]["CPT"][parents_requirement] if assignment[var] else 1 - network[var]["CPT"][parents_requirement])

    return p

def query(network, query_var, evidence):
    """
        Given a belief network, the name of a variable in the network, and some 
        evidence, returns the posterior distribution of query_var. The parameter 
        network is a belief network whose data structure was described earlier. 
        The parameter query_var is the name of the variable we are interested in 
        and is of type string. The parameter evidence is a dictionary whose 
        elements are assignments to some variables in the network; the keys are 
        the name of the variables and the values are Boolean.
    """
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Initialise a raw distribution to [0, 0]
    distribution = [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            # Update the assignment (we now have a complete assignment)
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            assignment = assignment | hidden_assignments
            # Update the raw distribution by the probability of the assignment.
            if not query_value:
                distribution[1] += joint_prob(network, assignment)
            else:
                distribution[0] += joint_prob(network, assignment)
    result = {True: distribution[0] / sum(distribution), False: distribution[1] / sum(distribution)}
    # Normalise the raw distribution and return it
    return result

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.3,
            (True,): 0.3
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.4,
            (True,): 0.5
            }},
}

print(sorted(network.keys()))

print(network['A']['Parents'])
print(network['B']['Parents'])
print(network['C']['Parents'])

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))