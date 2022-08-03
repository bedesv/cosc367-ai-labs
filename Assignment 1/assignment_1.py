from search import *
import re
import math

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
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == "S":
                    self.start_nodes.append((row, col, math.inf))
                elif re.match("[0-9]", self.map[row][col]):
                    self.start_nodes.append((row, col, int(self.map[row][col])))
                elif self.map[row][col] == "P":
                    self.portals.append((row, col))
    
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
        return 0 # as specified in Q2 

                

    def starting_nodes(self):
        return self.start_nodes



def main():
    """
        A main function
    """

    map_str = """\
    +------+
    |S    S|
    |  GXXX|
    |S     |
    +------+
    """

    graph = RoutingGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))


if __name__ == "__main__":
    main()