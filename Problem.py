
from Rubik import Rubik

ur = 0
ul = 1
lr = 2
ll = 3
fr = 4
fl = 5
rr = 6
rl = 7
dr = 8
dl = 9
br = 10
bl = 11

actions = [ur, ul, lr, ll, fr, fl, rr, rl, dr, dl, br, bl]

def child_node(node, action):
    rubik = Rubik([]) # fuck me :|
    for face in node.get_state():
            rubik.get_state().append(face.copy())
    rubik.move(action)
    return rubik

def goal_test(rubik):
    # check all elements in one side is equal, for all sides
    for face in rubik.get_state():
        if not all(elem == face[0] for elem in face):
            return False
    return True
