network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.6 # You can change this value
            }
        
    },

    'B': {
        'Parents': [],
        'CPT': {
            (): 0.5 # You can change this value
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
            (False,): 0.3,
            (True,): 0.4
            }
        
    },
    
    'E': {
        'Parents': ['B'],
        'CPT': {
            (False,): 0.2,
            (True,): 0.4
            }
        
    },
    
    
# add more variables

}
            
            