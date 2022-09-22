from turtle import pos
from search import *
from math import sqrt
import heapq

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes
    
    def outgoing_arcs(self, tail):
        arcs = []
        for possible_destination in sorted(self.location.keys()):
            if possible_destination != tail:
                dx = abs(self.location[tail][0] - self.location[possible_destination][0])
                dy = abs(self.location[tail][1] - self.location[possible_destination][1])
                distance = sqrt(dx**2+dy**2)
                if distance <= self.radius:
                    arcs.append(Arc(tail, possible_destination, f"{tail}->{possible_destination}", round(distance, 1)))
        return arcs

class LCFSFrontier(Frontier):
    def __init__(self):
        self.hqueue = []
        self.inserted = 0
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects.
        """
        total_cost = 0
        for arc in path:
            total_cost += arc.cost
        heapq.heappush(self.hqueue, (total_cost, self.inserted, path))
        self.inserted += 1

        
    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. If there nothing to return this should raise a
        StopIteration exception.
        """
        if len(self.hqueue) == 0:
            raise StopIteration
        return heapq.heappop(self.hqueue)[-1]
graph = ExplicitGraph(nodes=set('ABCD'),
                      edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                 ('B', 'C', 3), ('C', 'D', 1)],
                      starting_nodes=['A'],
                      goal_nodes={'D'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)