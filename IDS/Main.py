# created by _MuhmdrezA
# IDS algorithm for solving 2*2 rubik

_white = 0
_blue = 1
_green = 2
_orange = 3
_red = 4
_yellow = 5

initial_state = [[_yellow, _yellow, _white, _white], [_blue, _green, _red, _orange],
                 [_red, _orange, _green, _blue], [
                     _green, _blue, _red, _orange],
                 [_yellow, _white, _yellow, _white], [_green, _blue, _orange, _red]]


# for printing rubik
def print_rubik(rubik):
    print("[", end=" ")
    for face in rubik:
        print("[", end=" ")
        for elm in face:
            if (elm is _white):
                print("w,", end=" ")
            elif elm is _blue:
                print("b,", end=" ")
            elif elm is _red:
                print("r,", end=" ")
            elif elm is _green:
                print("g,", end=" ")
            elif elm is _yellow:
                print("y,", end=" ")
            elif elm is _orange:
                print("o,", end=" ")
        print("]", end=", ")
    print("]")


def update_states(rubic_state, index, direction):
    # fuck python, fuck call by reference :\.
    for face in range(len(rubic_state)):
        rubic_state[face] = rubic_state[face].copy()
    # for right turn direction must be 1 and for left turn must be -1
    if direction is 1:
        rubic_state[index][0:2], rubic_state[index][2:4] = rubic_state[index][2::-
                                                                              2], rubic_state[index][4:0:-2]
    else:
        rubic_state[index][0:2], rubic_state[index][2:
                                                    4] = rubic_state[index][1::2], rubic_state[index][0::2]

    # now rotate the neighbors.
    if index is 0:
        print("index was 0"+ str(direction))
        if direction is 1:  # rotate up to right
            rubic_state[1][0:2], rubic_state[2][0:2], rubic_state[3][0:2], rubic_state[5][2:
                                                                                          4] = rubic_state[2][0:2], rubic_state[3][0:2], rubic_state[5][3:1:-1], rubic_state[1][1::-1]
        else:  # rotate up tp left
            rubic_state[1][0:2], rubic_state[2][0:2], rubic_state[3][0:2], rubic_state[5][2:
                                                                                          4] = rubic_state[5][3:1:-1], rubic_state[1][0:2], rubic_state[2][0:2], rubic_state[3][1::-1]
    elif index is 1:
        print("index was 1 " + str(direction))
        if direction is 1:
            rubic_state[0][0:4:2], rubic_state[2][0:4:2], rubic_state[4][0:4:2], rubic_state[5][0:4:
                                                                                                2] = rubic_state[5][0:4:2], rubic_state[0][0:4:2], rubic_state[2][0:4:2], rubic_state[4][0:4:2]
        else:
            rubic_state[0][0:4:2], rubic_state[2][0:4:2], rubic_state[4][0:4:2], rubic_state[5][0:4:
                                                                                                2] = rubic_state[2][0:4:2], rubic_state[4][0:4:2], rubic_state[5][0:4:2], rubic_state[0][0:4:2]
    elif index is 2:
        print("index was 2" + str(direction))
        if direction is 1:
            rubic_state[0][2:4], rubic_state[1][1:4:2], rubic_state[4][0:2], rubic_state[3][0:4:
                                                                                            2] = rubic_state[1][3::-2], rubic_state[4][0:2], rubic_state[3][2::-2], rubic_state[0][2:4]
        else:
            rubic_state[0][2:4], rubic_state[1][1:4:2], rubic_state[4][0:2], rubic_state[3][0:4:
                                                                                            2] = rubic_state[3][0:4:2], rubic_state[0][4:1:-1], rubic_state[1][1:4:2], rubic_state[4][1::-1],
    elif index is 3:
        print("index was 3"+ str(direction))
        if direction is -1:
            rubic_state[0][1:4:2], rubic_state[2][1:4:2], rubic_state[4][1:4:2], rubic_state[5][1:4:
                                                                                                2] = rubic_state[5][1:4:2], rubic_state[0][1:4:2], rubic_state[2][1:4:2], rubic_state[4][1:4:2]
        else:
            rubic_state[0][1:4:2], rubic_state[2][1:4:2], rubic_state[4][1:4:2], rubic_state[5][1:4:
                                                                                                2] = rubic_state[2][1:4:2], rubic_state[4][1:4:2], rubic_state[5][1:4:2], rubic_state[0][1:4:2]
    elif index is 4:
        print("index was 4"+ str(direction))
        if direction is 1:
            rubic_state[1][2:4], rubic_state[2][2:4], rubic_state[3][2:4], rubic_state[5][0:
                                                                                          2] = rubic_state[5][1::-1], rubic_state[1][2:4], rubic_state[2][2:4], rubic_state[3][3:1:-1]
        else:
            rubic_state[1][2:4], rubic_state[2][2:4], rubic_state[3][2:4], rubic_state[5][0:
                                                                                          2] = rubic_state[2][2:4], rubic_state[3][2:4], rubic_state[5][1::-1], rubic_state[1][3:1:-1]
    elif index is 5:
        print("index was 5"+ str(direction))
        if direction is 1:
            rubic_state[0][0:2], rubic_state[1][0:4:2], rubic_state[4][2:4], rubic_state[3][1:4:
                                                                                            2] = rubic_state[3][1:4:2], rubic_state[0][1::-1], rubic_state[1][0:4:2], rubic_state[4][3:1:-1]
        else:
            rubic_state[0][0:2], rubic_state[1][0:4:2], rubic_state[4][2:4], rubic_state[3][1:4:
                                                                                            2] = rubic_state[1][2::-2], rubic_state[4][2:4], rubic_state[3][3::-2], rubic_state[0][0:2]
    return rubic_state


# UR, Rl, LR, LL, FR, FL, RR, RL, DR, DL, BR, BL
actions = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1),
           (3, 1), (3, -1), (4, 1), (4, -1), (5, 1), (5, -1)]


def goal_test(rubik):
    # check all elements in one side is equal, for all sides
    for face in rubik:
        if not all(elem == face[0] for elem in face):
            return False
    return True


def recursive_dls(node_state, limit):
    if goal_test(node_state):
        print("in goal state with limit " + str(limit))
        return node_state
    elif limit is 0:
        return -1
    else:
        cutoff = False
        for action in actions:
            child = update_states(node_state.copy(), action[0], action[1])
            print_rubik(child)
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
    return recursive_dls(initial_state, limit)


def iterative_deepning_search(limit):
    for i in range(limit + 1):
        print_rubik(initial_state)
        result = depth_limited_search(i)
        if result is not -1 and result is not None:
            return result
    return result


_limit = (int)(input("Enter the limit: "))
print(iterative_deepning_search(_limit))
