
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.001,
        }
    },
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.001,
        }
    },
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.001,
        }
    },
    'D': {
        'Parents': [],
        'CPT': {
            (): 0.001,
        }
    },

}

if __name__ == "__main__":
    from numbers import Number

    # Checking the overall type-correctness of the network
    # without checking anything question-specific

    assert type(network) is dict
    for node_name, node_info in network.items():
        assert type(node_name) is str
        assert type(node_info) is dict
        assert set(node_info.keys()) == {'Parents', 'CPT'}
        assert type(node_info['Parents']) is list
        assert all(type(s) is str for s in node_info['Parents'])
        for assignment, prob in node_info['CPT'].items():
            assert type(assignment) is tuple
            assert isinstance(prob, Number)

    print("OK")