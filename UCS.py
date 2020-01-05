from queue import PriorityQueue
from Problem import *
import heapq

class UCS():
    
    def __init__(self, initial_state):
        self.explored = []
        self.frontier = []
        self.initial_rubik = initial_state
    
    def UCS(self):
        heapq.heappush(self.frontier, self.initial_rubik)
        while True:       
            if len(self.frontier) == 0: return None
            node = heapq.heappop(self.frontier)
            if goal_test(node): 
                return node
            if node not in self.explored:
                self.explored.append(node)
            for action in actions:
                child = child_node(node, action)
                child.path_cost = node.path_cost + 1 
                if child not in self.explored and child not in self.frontier: 
                    print(" not in frontier and explore ")
                    heapq.heappush(self.frontier, child)
                elif child in self.frontier:
                    self.frontier.remove(child)
                    heapq.heappush(self.frontier, child)
                    # self.frontier[self.frontier.index(child)].path_cost = child.path_cost # another way
                    heapq.heapify(self.frontier)