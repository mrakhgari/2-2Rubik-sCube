# created by _MuhmdrezA
# IDS algorithm for solving 2*2 rubik

from Problem import *
from Rubik import *


_white = 0
_blue = 1
_green = 2
_orange = 3
_red = 4
_yellow = 5

initial_rubik = Rubik()
initial_rubik.set_state([[_yellow, _yellow, _white, _white], [_blue, _green, _red, _orange],
                 [_red, _orange, _green, _blue], [
                     _green, _blue, _red, _orange],
                 [_yellow, _white, _yellow, _white], [_green, _blue, _orange, _red]])



def recursive_dls(node_state, limit):
    if goal_test(node_state):
        print("in goal state with limit " + str(limit))
        return node_state
    elif limit is 0:
        return -1
    else:
        cutoff = False
        for action in actions:
            child = child_node(node_state, action)
            print("child " + child.__str__())
            result = recursive_dls(child, limit-1)
            if result is -1:
                cutoff = True
            elif result is not None:
                return result
        if cutoff is True:
            return -1
        else:
            return False


def depth_limited_search(limit):
    return recursive_dls(initial_rubik, limit)


def iterative_deepning_search(limit):
    for i in range(limit + 1):
        print("in the ids with i " + str(i) + "#################################3")
        print(initial_rubik)
        result = depth_limited_search(i)
        if result is not -1 and result is not None:
            return result
    return result


_limit = (int)(input("Enter the limit: "))
print(iterative_deepning_search(_limit))
