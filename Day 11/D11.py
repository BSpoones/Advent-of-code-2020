import time
startTime = time.time()

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
while True:
    New_Grid = []
    for i,lst in enumerate(Grid):
        New_List = []
        for j,item in enumerate(lst):
            Position =Pos(i,j)
            if Position.check() == "L":
                New_List.append("L")
            elif Position.check() == "#":
                New_List.append("#")
            else:
                New_List.append(Position.POS)
        New_Grid.append(New_List)
                
    
    count = 0
    for lst in New_Grid: 
        for item in lst:
            count += item.count("#")
    Grid = New_Grid
    if count == lastcount:
        break
    lastcount = count
print("Part 1:",count)

print(time.time()-startTime)


def load(arr: list):
    with open("Seats.txt", 'r') as file:
        for line in file.readlines():
            line = line.strip()
            arr.append([char for char in line])


def process(arr: list):
    temp = []
    for x in range(len(arr)):
        temp.append([])
        for y in range(len(arr[x])):
            if arr[x][y] == ".":
                temp[x].append(".")
            else:
                if arr[x][y] == "L":
                    temp[x].append("#" if apply(arr, x, y) == 0 else "L")
                else:
                    temp[x].append("L" if apply(arr, x, y) >= 4 else "#")
    return temp


def apply(arr, i, j):
    sect = list(x[max(j-1, 0): j+2] for x in arr[max(i-1, 0): i+2])
    return sum([b.count("#") for b in sect]) - (1 if arr[i][j] == "#" else 0)


def main():
    arr = []
    load(arr)
    new = process(arr)
    while new != arr:
        arr = new
        new = process(arr)
    count = sum(len(list(x)) for x in list(map(lambda x: filter(
        lambda y: y == "#", x), arr)))
    print(count)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main", number=1))
input()