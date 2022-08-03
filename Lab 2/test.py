from search import Arc
from student_answer import LCFSFrontier

frontier = LCFSFrontier()
frontier.add((Arc(None, None, None, 17),))
frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

for path in frontier:
    print(path)

from search import *
from student_answer import LocationGraph, LCFSFrontier

graph = LocationGraph(
    location={'A': (25, 7),
              'B': (1, 7),
              'C': (13, 2),
              'D': (37, 2)},
    radius=15,
    starting_nodes=['B'],
    goal_nodes={'D'}
)

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

from search import *
from student_answer import LCFSFrontier

graph = ExplicitGraph(nodes=set('ABCD'),
                      edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                 ('B', 'C', 3), ('C', 'D', 1)],
                      starting_nodes=['A'],
                      goal_nodes={'D'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)