network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    'D': {
        'Parents': ['B'],
        'CPT': {
            (False,): 0.4, # Doesn't matter what values are in D and E
            (True,): 0.5   # provided they're both different as it means
            }              # they're dependent on B
        
    },
    'E': {
        'Parents': ['B'],
        'CPT': {
            (False,): 0.4,
            (True,): 0.3
            }
        
    },

}