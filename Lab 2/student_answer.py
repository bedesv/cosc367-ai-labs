import heapq
from search import Arc, Graph, Frontier
from math import sqrt

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
        tail_location = self.location[tail]
        for head, head_location in self.location.items():
            x_vector = abs(tail_location[0] - head_location[0])
            y_vector = abs(tail_location[1] - head_location[1])
            distance = sqrt(x_vector ** 2 + y_vector ** 2)
            if distance <= self.radius and head is not tail:
                arcs.append(Arc(tail=tail, head=head, action=f"{tail}->{head}", cost=distance))
        return sorted(arcs, key=lambda x: x.head)

class LCFSFrontier(Frontier):

    def __init__(self):
        self.key = lambda x: (x[0].cost, x[1])
        self.queue = []
        self.index = 0
        self.expanded = set()

    def add(self, path):
        """
            Adds the given path to the frontier
        """
        cost = 0
        for arc in path:
            cost += arc.cost
        heapq.heappush(self.queue, [cost, self.index, path])
        self.index += 1

    def __next__(self):
        """
            Returns the next object in the frontier
        """
        if len(self.queue) <= 0:
            raise StopIteration
        next = heapq.heappop(self.queue)
        
        return next[-1]
