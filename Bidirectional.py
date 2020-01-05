from Rubik import * 
from Problem import *

class Bidirectional:
    def __init__(self, initial_state):
        self.forward_queue = []
        self.backward_queue = []
        self.rubik_state = initial_state
        self.__get_final_state()
        self.forward_visited = []
        self.backward_visited = []

    def __get_final_state(self):
        self.final_state = Rubik([])
        rubik = []
        for color in colors:
            self.final_state.get_state().append([color]*4)
    
    def Bidirectional(self):
        self.forward_queue.append(self.rubik_state)
        self.backward_queue.append(self.final_state)
        while len(self.backward_queue) != 0 and len(self.forward_queue) != 0:
            if len(self.forward_queue) != 0:
                x = self.forward_queue.pop(0)
                if x == self.final_state or x in self.backward_queue:
                    return True
                for action in actions:
                    child = child_node(x, action)
                    if child not in self.backward_visited and child not in self.forward_visited:
                        self.forward_visited.append(child)
                        self.forward_queue.append(child)
                    elif child in self.backward_visited: return True
            if len(self.backward_queue) != 0:
                x = self.backward_queue.pop(0)
                if x == self.rubik_state or x in self.forward_queue:
                    return True
                for action in actions:
                    child = child_node(x, action)
                    if child not in self.backward_queue and child not in self.forward_visited:
                        self.backward_visited.append(child)
                        self.backward_queue.append(child)
                    elif child in self.forward_visited: return True        
        return False
