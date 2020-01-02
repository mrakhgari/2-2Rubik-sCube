# created by _MuhmdrezA

states = [[4, 4, 2, 2], [1, 3, 5, 6], [1, 1, 5, 5],
          [6, 3, 6, 3], [4, 2, 2, 4], [3, 1, 6, 5]]


def update_states(states, index, direction):
    # for right turn direction must be 1 and for left turn must be -1
    if direction is 1 :
        states[index][0:2], states[index][2:4] = states[index][2::-2], states[index][4:0:-2]
    else:
        states[index][0:2], states[index][2:4] = states[index][1::2], states[index][0::2]
  
    # now rotate the neighbors.
    if index is 0:
        print("index was 1")
        if direction is 1:  # rotate up to right
            states[1][0:2], states[2][0:2], states[3][0:2], states[5][2:
                                                                      4] = states[2][0:2], states[3][0:2], states[5][2:4], states[1][0:2]
        else:  # rotate up tp left
            states[1][0:2], states[2][0:2], states[3][0:2], states[5][2:
                                                                      4] = states[5][2:4], states[1][0:2], states[2][0:2], states[3][0:2]
    elif index is 1:
        if direction is 1:
            print("rotate right, left side")
            states[0][0:4:2], states[2][0:4:2], states[4][0:4:2], states[5][0:4:
                                                                            2] = states[5][0:4:2], states[0][0:4:2], states[2][0:4:2], states[4][0:4:2]
        else:
            print("rotate left, left side")
            states[0][0:4:2], states[2][0:4:2], states[4][0:4:2], states[5][0:4:
                                                                            2] = states[2][0:4:2], states[4][0:4:2], states[5][0:4:2], states[0][0:4:2]
    elif index is 2:
        if direction is 1:
            states[0][2:4], states[1][1:4:2], states[4][0:2], states[3][0:4:
                                                                        2] = states[1][1:4:2], states[4][0:2], states[3][0:4:2], states[0][2:4]
        else:
            states[0][2:4], states[1][1:4:2], states[4][0:2], states[3][0:4:
                                                                        2] = states[3][0:4:2], states[0][2:4], states[1][1:4:2], states[4][0:2],
    elif index is 3:
        if direction is -1:
            states[0][1:4:2], states[2][1:4:2], states[4][1:4:2], states[5][1:4:
                                                                            2] = states[5][1:4:2], states[0][1:4:2], states[2][1:4:2], states[4][1:4:2]
        else:
            states[0][1:4:2], states[2][1:4:2], states[4][1:4:2], states[5][1:4:
                                                                            2] = states[2][1:4:2], states[4][1:4:2], states[5][1:4:2], states[0][1:4:2]
    elif index is 4:
        if direction is 1:
            states[1][2:4], states[2][2:4], states[3][2:4], states[5][0:
                                                                      2] = states[5][0:2], states[1][2:4], states[2][2:4], states[3][2:4]
        else:
            states[1][2:4], states[2][2:4], states[3][2:4], states[5][0:
                                                                      2] = states[2][2:4], states[3][2:4], states[5][0:2], states[1][2:4]
    elif index is 5:
        if direction is 1:
            states[0][0:2], states[1][0:4:2], states[4][2:4], states[3][1:4:
                                                                        2] = states[3][1:4:2], states[0][0:2], states[1][0:4:2], states[4][2:4]
        else:
            states[0][0:2], states[1][0:4:2], states[4][2:4], states[3][1:4:
                                                                        2] = states[1][0:4:2], states[4][2:4], states[3][1:4:2], states[0][0:2]


_limit = map(int, input("Enter the limit: "))

