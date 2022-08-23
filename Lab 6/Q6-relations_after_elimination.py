from csp import *


csp = CSP(
   var_domains = {var:{-1,0,1} for var in 'abcd'},
   constraints = {
      lambda a, b: a == abs(b),
      lambda c, d: c > d,
      lambda a, b, c: a * b > c + 1
      }
   )

from csp import Relation

relations = [

    Relation(
        header=['a', 'b'],
        tuples={(1, 1),
                (1, -1),
                (0, 0)
                }
    ),

    Relation(
        header=['c', 'd'],
        tuples={(0, -1),
                (1, -1),
                (1, 0)
                }
    ),

    Relation(
        header=['a', 'b', 'c'],
        tuples={(1, 1, -1),
                (-1, -1, -1)
                }
    )

]

relations_after_elimination = [

    Relation(
        header=['b'],
        tuples={(1,),
                (-1,),
                (0,)
                }
    ),

    Relation(
        header=['c', 'd'],
        tuples={(0, -1),
                (1, -1),
                (1, 0)
                }
    ),

    Relation(
        header=['b', 'c'],
        tuples={(1, -1)
                }
    )

]
