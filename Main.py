from UCS import UCS 
from Rubik import Rubik
from Bidirectional import *


rubik_sides = []

_white = 0
_blue = 1
_green = 2
_orange = 3
_red = 4
_yellow = 5

rubik = Rubik([[_yellow, _yellow, _white, _white], [_blue, _green, _blue, _green],
                 [_red, _red, _red, _red], [
                     _blue, _green, _blue, _green],
                 [_yellow, _yellow, _white, _white], [_orange, _orange, _orange, _orange]])


# for i in range(6):
    # rubik_sides.append(list(map(int, input().split())))

# rubik = Rubik(rubik_sides)

# ucs = UCS(rubik)
# ucs.UCS()
Bidirectional(rubik)
# print(rubik)