with open("Directions.txt") as f:
    content = f.read()
    DirectionList = content.split("\n")

CurrentFacing = 90
N,E = 0,0
class Direction:
    def __init__(self,Direction):
        self.Type = Direction[0]
        self.Magnitude = int(Direction[1:])

    def check(self):
        global CurrentFacing,N,E
        if CurrentFacing == 360:
            CurrentFacing = 0

        if self.Type == "N":
            N += self.Magnitude
        elif self.Type == "S":
            N -= self.Magnitude
        elif self.Type == "E":
            E += self.Magnitude
        elif self.Type == "W":
            E -= self.Magnitude
        
        if self.Type == "L":
            if CurrentFacing-self.Magnitude <0:
                CurrentFacing = 360 + CurrentFacing
            CurrentFacing -= self.Magnitude
        elif self.Type == "R":
            if CurrentFacing + self.Magnitude >= 360:
                CurrentFacing += self.Magnitude -360
            else:
                CurrentFacing += self.Magnitude
        
        if self.Type == "F":
            if CurrentFacing == 0:
                N += self.Magnitude
            elif CurrentFacing == 90:
                E += self.Magnitude
            elif CurrentFacing == 180:
                N -= self.Magnitude
            elif CurrentFacing == 270:
                E -= self.Magnitude
            
for item in DirectionList:
    temp = Direction(item)
    temp.check()
print("Part 1:",abs(N)+abs(E))