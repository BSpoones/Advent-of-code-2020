import time, multiprocessing
from multiprocessing import Pool
with open("Seats.txt") as f:
    content = f.read()
    SeatsList = content.split("\n")

Grid = []
New_Grid = []
for i,val in enumerate(SeatsList):
    row = list(SeatsList[i])
    Grid.append(row)


class Pos:
    def __init__(self,i,j):
        self.POS = Grid[i][j]
        try:
            if i-1<0 or j-1<0:
                raise ValueError 
            self.TOP_LEFT = Grid[i-1][j-1]
        except: self.TOP_LEFT = "0"

        try:
            if i-1<0 or j<0:
                raise ValueError
            self.TOP_MIDDLE = Grid[i-1][j]
        except: self.TOP_MIDDLE = "0"

        try: 
            if i-1<0 or j<0:
                raise ValueError
            self.TOP_RIGHT = Grid[i-1][j+1]
        except: self.TOP_RIGHT = "0"

        try: 
            if i<0 or j-1<0:
                raise ValueError
            self.MIDDLE_LEFT = Grid[i][j-1]
        except: self.MIDDLE_LEFT = "0"
        
        try: self.MIDDLE_RIGHT = Grid[i][j+1]
        except: self.MIDDLE_RIGHT = "0"

        try: 
            if i<0 or j-1<0:
                raise ValueError
            self.BOTTOM_LEFT = Grid[i+1][j-1]
        except: self.BOTTOM_LEFT = "0"

        try: self.BOTTOM_MIDDLE = Grid[i+1][j]
        except: self.BOTTOM_MIDDLE = "0"

        try: self.BOTTOM_RIGHT = Grid[i+1][j+1]
        except: self.BOTTOM_RIGHT = "0"

        self.ADJACENT = [self.TOP_LEFT,self.TOP_MIDDLE,self.TOP_RIGHT,self.MIDDLE_LEFT,self.MIDDLE_RIGHT,self.BOTTOM_LEFT,self.BOTTOM_MIDDLE,self.BOTTOM_RIGHT]

    def check(self):
        self.HASHcount = 0
        for char in self.ADJACENT:
            self.HASHcount += char.count("#")
        if self.POS == "L":
            if self.HASHcount == 0:
                return "#"
        if self.POS == "#":
            if self.HASHcount >=4:
                return "L"

lastcount = 0
def compare(i,lst):
    New_List = []
    for j, item in enumerate(lst):
        Position =Pos(i,j)
        if Position.check() == "L":
            New_List.append("L")
        elif Position.check() == "#":
            New_List.append("#")
        else:
            New_List.append(Position.POS)
    return New_List
    
while True:
    New_Grid = []

    NewList = map([compare(i,lst) for i,lst in enumerate(Grid)])
    New_Grid.append(NewList)


    # for i,lst in enumerate(Grid):
    #     New_List = []
    #     for j,item in enumerate(lst):
    #         Position =Pos(i,j)
    #         if Position.check() == "L":
    #             New_List.append("L")
    #         elif Position.check() == "#":
    #             New_List.append("#")
    #         else:
    #             New_List.append(Position.POS)
    #     New_Grid.append(New_List)
                
    
    count = 0
    for lst in New_Grid: 
        for item in lst:
            count += item.count("#")
    Grid = New_Grid
    if count == lastcount:
        break
    lastcount = count
print("Part 1:",count)