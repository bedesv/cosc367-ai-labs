from search import *
import re
import math
import heapq

class RoutingGraph(Graph):
    """
        A routing graph class
    """

    def __init__(self, map_str):
        """
            Initialises the graph using a map string
        """
        self.map = [[char for char in line.strip()] for line in map_str.splitlines() if line.strip() != ""]

        self.start_nodes = []
        self.portals = []
        self.goal_nodes = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == "S":
                    self.start_nodes.append((row, col, math.inf))
                elif re.match("[0-9]", self.map[row][col]):
                    self.start_nodes.append((row, col, int(self.map[row][col])))
                elif self.map[row][col] == "P":
                    self.portals.append((row, col))
                elif self.map[row][col] == "G":
                    self.goal_nodes.append((row, col))
    
    def is_goal(self, node):
        x_coord = node[0]
        y_coord = node[1]
        return self.map[x_coord][y_coord] == "G"

    def get_teleport_moves(self, current_pos):
        teleport_moves = []
        for portal in self.portals:
            if portal != tuple(current_pos):
                teleport_moves.append(portal)
        return teleport_moves

    def outgoing_arcs(self, tail_node):
        possible_moves = [('N' , -1, 0),
                         ('E' ,  0, 1),
                         ('S' ,  1, 0),
                         ('W' ,  0, -1),]
        arcs = []
        current_pos = [tail_node[0], tail_node[1]]
        current_fuel = tail_node[2]
        for move in possible_moves:
            next_pos_x = current_pos[0] + move[1]
            next_pos_y = current_pos[1] + move[2]
            if self.map[next_pos_x][next_pos_y] in ["-", "|", "+", "X"] or current_fuel == 0:
                continue
            else:
                head_node = (next_pos_x, next_pos_y, current_fuel - 1)
                arcs.append(Arc(tail_node, head_node, move[0], 5))

        if self.map[current_pos[0]][current_pos[1]] == "P":
            for teleport_move in self.get_teleport_moves(current_pos):
                head_node = (teleport_move[0], teleport_move[1], current_fuel)
                arcs.append(Arc(tail_node, head_node, "Teleport to " + str(teleport_move), 10))
        elif self.map[current_pos[0]][current_pos[1]] == "F" and current_fuel < 9:
            head_node = (current_pos[0], current_pos[1], 9)
            arcs.append(Arc(tail_node, head_node, "Fuel up", 15))
        return arcs

    def estimated_cost_to_goal(self, node):
        estimates = []
        for goal in self.goal_nodes:
            estimate = abs(goal[0]-node.head[0]) + abs(goal[1]-node.head[1])
            estimates.append(estimate)
        return min(estimates) * 5

    def starting_nodes(self):
        return self.start_nodes

class AStarFrontier(Frontier):
    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        self.index = 0
        self.expanded = set()
        
    def add(self, path):
        cost  = 0
        next_location = path[-1]
        if next_location not in self.expanded:
            for arc in path:
                cost += arc.cost
            cost += self.graph.estimated_cost_to_goal(path[-1])
            heapq.heappush(self.queue, [cost, self.index, path])
            self.index += 1

    def __next__(self):
        """
            Returns the next object in the frontier
        """
        if len(self.queue) <= 0:
            raise StopIteration
        next = heapq.heappop(self.queue)
        next_location = next[-1][-1]
        
        while next_location in self.expanded:
            if len(self.queue) <= 0:
                raise StopIteration
            next = heapq.heappop(self.queue)
            next_location = next[-1][-1]
        self.expanded.add(next_location)
        return next[-1]
        

def print_map(map_graph, frontier, solution):
    """
        takes three parameters: an instance of RoutingGraph, an instance of AStarFrontier which has just been used to run a graph search on the given graph, and the result of the search, and then prints a map such that:

        the position of the walls, obstacles, agents, and the goal points are all unchanged and they are marked by the same set of characters as in the original map string;
        those free spaces (space characters) that have been expanded during the search are marked with a '.' (a period character); and
        those free spaces (spaces characters) that are part of the solution (best path to the goal) are marked with '*' (an asterisk character).
    """

    map = map_graph.map
    solution_indices = [(x.head[0], x.head[1]) for x in solution] if solution else []
    expanded_indices = [(x.head[0], x.head[1]) for x in frontier.expanded]

    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] not in ["S", "G"]:
                if (row, col) in solution_indices:
                    map[row][col] = "*"
                elif (row, col) in expanded_indices:
                    map[row][col] = "."

    map = "\n".join(["".join(x) for x in map])
    print(map)


map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)