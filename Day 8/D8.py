with open("Instructions.txt") as f:
    content = f.read()
    Instruction_List = content.split("\n")
accVal = 0
position = 0
used = []

def check(myList):
    global position, accVal, current
    accVal = 0
    while True:
        try:
            if position in used:
                break
            else:
                used.append(position)
                current = (myList[position])
                if current[:3] == "acc":
                    if current[4] == "+":
                        accVal += int(current[5:])
                    elif current[4] == "-":
                        accVal -= int(current[5:])
                    position += 1
                if current[:3] == "jmp":
                    if current[4] == "+":
                        position += int(current[5:])
                    elif current[4] == "-":
                        position -= int(current[5:])
                if current[:3] == "nop":
                    position += 1
        except:
            global currentVal
            currentVal = accVal
            break
    pass

check(Instruction_List)
print("Part 1:",accVal)

#Part 2:
for i, val in enumerate(Instruction_List):
    accVal = 0
    position = 0
    Temp_List = Instruction_List.copy()
    used = []
    if val[:3] == "jmp":
        Temp_List[i] = "nop" + val[3:]
    check(Temp_List)
for i,val in enumerate(Instruction_List):
    accVal = 0
    position = 0
    Temp_List = Instruction_List.copy()

    used = []
    if val[:3] == "jmp":
        Temp_List[i] = "nop" + val[3:]
    check(Temp_List)
print("Part 2:",currentVal)

    
