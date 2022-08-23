from csp import *

csp = CSP(
    var_domains={var: {0, 1, 2} for var in 'abcd'},
    constraints={
        lambda a, b, c: a > b + c,
        lambda c, d: c > d
    }
)

# from csp import Relation

relations = [
    Relation(
        header=['a', 'b', 'c'],
        tuples={(2, 0, 1),
                (2, 1, 0),
                (2, 0, 0),
                (1, 0, 0)
                }
    ),

    Relation(
        header=['c', 'd'],
        tuples={(1, 0),
                (2, 0),
                (2, 1)
                }
    )
]

print(len(relations))
print(all(type(r) is Relation for r in relations))
