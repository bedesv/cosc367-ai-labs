from search import *
import heapq


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.num_inserted = 0
        

    def add(self, path):
        cost = 0
        for arc in path:
            cost += arc.cost
        heapq.heappush(self.container, (cost, self.num_inserted, path))
        self.num_inserted += 1

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return heapq.heappop(self.container)[-1]
        else:
            raise StopIteration   # don't change this one    
    


if __name__ == "__main__":
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'G'},
        edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
        starting_nodes = ['S'],
        goal_nodes = {'G'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)