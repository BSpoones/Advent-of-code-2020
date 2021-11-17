with open("Seats.txt") as f:
    content = f.read()
    SeatList = content.split("\n")

seatIDs = []
for item in (SeatList):
    rows = [j for j in range(128)]
    cols = [k for k in range(8)]
    for char in item:
        halfway = int(len(rows)/2)
        halfway2 = int(len(cols)/2)
        if len(rows) ==2:
            halfway = 1
        if char == "F":    
            rows = rows[:halfway]
        if char == "B":
            rows = rows[halfway:]
        if char == "L":
            cols = cols[:halfway2]
        if char == "R":
            cols = cols[halfway2:]
    seatIDs.append((rows[0]*8)+cols[0])
seatIDs.sort()
print("Part 1:",max(seatIDs))
for i in range(max(seatIDs)):
    if int(i+1)in seatIDs and i-1 in seatIDs:
        if i not in seatIDs:
            print("Part 2:",i)

