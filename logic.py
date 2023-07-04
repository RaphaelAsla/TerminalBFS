from queue import Queue
import os
import time

class Graph:
    def __init__(self, graph):
            self.graph = graph

    def get_height(self):
        return len(self.graph)  

    def get_width(self):
        return len(self.graph[0])

    def at(self, row, col):
        return self.graph[row][col]

    def insert_at(self, row, col, val):
        self.graph[row][col] = val

    def find_neighbors(self, node):
        neighbors = []
        row, col = node
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for d in directions:
            drow = row + d[0]
            dcol = col + d[1]
            if (drow >= 0 and drow < len(self.graph) and dcol >= 0 and dcol < len(self.graph[row])):
                neighbors.append((drow, dcol))
        return neighbors

    def find_first(self, val):
        for i in range(self.get_height()):
            for j in range(len(self.graph[i])):
                if self.at(j, i) == val:
                    return (i, j)
        return (None, None)

    def print(self):
        for row in self.graph:
            for val in row:
                print(val, end='')
            print()

class BFS:
    def __init__(self, graph: Graph):
        self.frontier = Queue()
        self.came_from = dict()
        self.shortest_path = []
        self.graph = graph

    def search(self, start_node, goal_node, obstacles):
        self.start_node = start_node
        self.goal_node = goal_node
        self.came_from[start_node] = None
        self.frontier.put(start_node)
        current_node = start_node
        solvable = False
        while not self.frontier.empty():
            current_node = self.frontier.get()
            if current_node == goal_node:
                solvable = True
                break
            for next_node in self.graph.find_neighbors(current_node):
                if self.graph.at(next_node[0], next_node[1]) in obstacles:
                    continue
                elif next_node not in self.came_from:
                    os.system("clear")
                    self.graph.insert_at(next_node[0], next_node[1], '🟩') 
                    self.graph.print()
                    self.graph.insert_at(next_node[0], next_node[1], '🟦') 
                    time.sleep(0.01)
                    self.frontier.put(next_node)
                    self.came_from[next_node] = current_node
        return solvable

    def get_path(self):
        current_node = self.goal_node
        while current_node != self.start_node:
           self.shortest_path.append(current_node)
           current_node = self.came_from[current_node]
        self.shortest_path.append(self.start_node)
        return reversed(self.shortest_path)
