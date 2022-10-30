network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.2,
            (True,): 0.3
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.4,
            (True,): 0.4
            }},
}
