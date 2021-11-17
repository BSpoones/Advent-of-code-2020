with open("Slope.txt") as f:
    content = f.read()
    Lines = content.split("\n")
global Trees
Trees = 0

Grid = []
for i,val in enumerate(Lines):
    row = (list(Lines[i]))
    Grid.append(row)
print(Grid)

i=0
j=0


def checkLocation(i,j):
    global Trees
    if Grid[i][j] == "#":
        Grid[i][j] = "X"
        Trees += 1
        print("Tree found at",i,j)
    else:
        Grid[i][j] = "O"

while True:
    try:
        i +=1   #Down
        j +=3   #Right
        if j > 30:
            j = j-31
        print("Checking",i,j)
        checkLocation(i,j)
    except:
        print(Trees)
        break


#R1D1 = 90
#R3D1 = 274
#R5D1 = 82
#R7D1 = 68
#R1D2 = 44
