# created by _MuhmdrezA
# IDS algorithm for solving 2*2 rubik

from Problem import *

class IDS():
    def __init__(self, inital_state = [], limit = 0):
        self.limit = limit
        self.initial_rubik = inital_state

    def recursive_dls(self, node_state, limit):
        if goal_test(node_state):
            return node_state
        elif limit is 0:
            return None
        else:
            for action in actions: 
                result = recursive_dls(child_node(node_state, action), limit-1)
                if result is not None :
                    return result
            return result

    def depth_limited_search(self, limit):
        return recursive_dls(initial_rubik, limit)


    def iterative_deepning_search(self):
        for i in range(self.limit + 1):
            result = depth_limited_search(i)
            if result is not None:
                return result
        return result

