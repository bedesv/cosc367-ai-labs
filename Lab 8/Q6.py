
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.3, # Making these values the same means that
            (True,): 0.3   # the result of B does not change with A
            }},            # and so it must be independent
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.4,
            (True,): 0.5
            }},
}
