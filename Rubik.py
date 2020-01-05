from Problem import *
# rubik class


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

_white = 0
_blue = 1
_green = 2
_orange = 3
_red = 4
_yellow = 5

class Rubik:

    def __init__(self):
        self.__state = [] 
    
    def __repr__(self):
        return "Rubik instance"

    def __eq__(self, other):
        if not isinstance(other, Rubik):
            return NotImplemented
        return self.__state == other.__state

    def __hash__(self):
        return hash(self.__state)

    def __str__(self):
        text = "["
        for face in self.__state:
            text += "["
            for elm in face:
                if (elm is _white):
                    text += "w, "
                elif elm is _blue:
                    text += "b, "
                elif elm is _red:
                    text += "r, "
                elif elm is _green:
                    text += "g, "
                elif elm is _yellow:
                    text += "y, "
                elif elm is _orange:
                    text += "o, "
            text += "],"
        text += "]"
        return text

    def __move_ur(self):
        print("in the move ur")
        self.__state[1][0:2], self.__state[2][0:2], self.__state[3][0:2], self.__state[5][2:
                                                                                          4] = self.__state[2][0:2], self.__state[3][0:2], self.__state[5][3:1:-1], self.__state[1][1::-1]
    
    def __move_ul(self):
        print("in the move ul")
        self.__state[1][0:2], self.__state[2][0:2], self.__state[3][0:2], self.__state[5][2:
                                                                                          4] = self.__state[5][3:1:-1], self.__state[1][0:2], self.__state[2][0:2], self.__state[3][1::-1]
   
    def __move_lr(self):
        print("in the move left side, right direction")
        self.__state[0][0:4:2], self.__state[2][0:4:2], self.__state[4][0:4:2], self.__state[5][0:4:
                                                                                                2] = self.__state[5][0:4:2], self.__state[0][0:4:2], self.__state[2][0:4:2], self.__state[4][0:4:2]
    
    def __move_ll(self):
        print("in the move left side, left direction")
        self.__state[0][0:4:2], self.__state[2][0:4:2], self.__state[4][0:4:2], self.__state[5][0:4:
                                                                                                2] = self.__state[2][0:4:2], self.__state[4][0:4:2], self.__state[5][0:4:2], self.__state[0][0:4:2]
    
    def __move_fr(self):
        print("in the move face side, right direction")
        self.__state[0][2:4], self.__state[1][1:4:2], self.__state[4][0:2], self.__state[3][0:4:
                                                                                            2] = self.__state[1][3::-2], self.__state[4][0:2], self.__state[3][2::-2], self.__state[0][2:4]
        
    def __move_fl(self):
        print("in the move face side, left direction")
        self.__state[0][2:4], self.__state[1][1:4:2], self.__state[4][0:2], self.__state[3][0:4:
                                                                                            2] = self.__state[3][0:4:2], self.__state[0][4:1:-1], self.__state[1][1:4:2], self.__state[4][1::-1],
    
    def __move_rr(self):
        print("in the move right side, right direction")
        self.__state[0][1:4:2], self.__state[2][1:4:2], self.__state[4][1:4:2], self.__state[5][1:4:
                                                                                                2] = self.__state[5][1:4:2], self.__state[0][1:4:2], self.__state[2][1:4:2], self.__state[4][1:4:2]
  
    def __move_rl(self):
        print("in the move right side, left direction")
        self.__state[0][1:4:2], self.__state[2][1:4:2], self.__state[4][1:4:2], self.__state[5][1:4:
                                                                                                2] = self.__state[2][1:4:2], self.__state[4][1:4:2], self.__state[5][1:4:2], self.__state[0][1:4:2]
    
    def __move_dr(self):
        print("in the move down side, right direction")
        self.__state[1][2:4], self.__state[2][2:4], self.__state[3][2:4], self.__state[5][0:
                                                                                          2] = self.__state[5][1::-1], self.__state[1][2:4], self.__state[2][2:4], self.__state[3][3:1:-1]
  
    def __move_dl(self):
        print("in the move down side, left direction")
        self.__state[1][2:4], self.__state[2][2:4], self.__state[3][2:4], self.__state[5][0:
                                                                                          2] = self.__state[2][2:4], self.__state[3][2:4], self.__state[5][1::-1], self.__state[1][3:1:-1]
  
    def __move_br(self):
        print("in the move back side, right direction")
        self.__state[0][0:2], self.__state[1][0:4:2], self.__state[4][2:4], self.__state[3][1:4:
                                                                                            2] = self.__state[3][1:4:2], self.__state[0][1::-1], self.__state[1][0:4:2], self.__state[4][3:1:-1]
  
    def __move_bl(self):
        print("in the move back side, left direction")
        self.__state[0][0:2], self.__state[1][0:4:2], self.__state[4][2:4], self.__state[3][1:4:
                                                                                            2] = self.__state[1][2::-2], self.__state[4][2:4], self.__state[3][3::-2], self.__state[0][0:2]
    
    def move(self,action):
        if action % 2 == 0:
                self.__state[action//2][0:2], self.__state[action//2][2:4] = self.__state[action//2][2::-2], self.__state[action//2][4:0:-2]
        else:
                self.__state[action//2][0:2], self.__state[action//2][2:4] = self.__state[action//2][1::2], self.__state[action//2][0::2]

        if action is ur:
            self.__move_ur()
        elif action is ul:
            self.__move_ul()
        elif action is lr: self.__move_lr()
        elif action is ll: self.__move_ll()
        elif action is fr: self.__move_fr()
        elif action is fl: self.__move_fl()
        elif action is rr: self.__move_rr()
        elif action is rl: self.__move_rl()
        elif action is dr: self.__move_dr()
        elif action is dl: self.__move_dl()
        elif action is br: self.__move_br()
        elif action is bl: self.__move_bl()
        
    def get_state(self):
        return self.__state

    def set_state(self, faces):
        self.__state = faces