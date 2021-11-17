with open("Adapters.txt") as f:
    content = f.read()
    Adapters_List = content.split("\n")

print(f'Total amount of adapters in your bag: {len(Adapters_List)}')

"""
Each Jolt value in the list must be 1,2 or 3 larger than the one before it
Final value must be 3 higher than the highest in the list
Calculating how many 1 and 3 jolt differences there are
Aim of trying not to skip any adapters
Only skipping 2 as a last resort
"""

#Sorting the list 
Adapters_List = sorted([int(val) for val in Adapters_List])

One = 0
Two = 0
Three = 1 #Starts at 1 because the TopVal is 3 higher
TopVal = max(Adapters_List)+3
PreviousVal = 0

#Going through list
for i,val in enumerate(Adapters_List):
    if val - PreviousVal == 1:
        PreviousVal = val
        One += 1
    if val - PreviousVal == 3:
        PreviousVal = val
        Three +=1

print("Part 1:",One*Three)

#Part 2

"""
Finding every way to get from 0 to TopVal
Not all adapters have to be included
Can skip 1,2 or 3 adapters

If val +1,2,3 in list
Make 1,2, or 3 different checks for each item
"""

sol = {0:1}
for line in Adapters_List:
    sol[line] = 0
    if line - 1 in sol:
        sol[line]+=sol[line-1]
    if line - 2 in sol:
        sol[line]+=sol[line-2]
    if line - 3 in sol:
        sol[line]+=sol[line-3]
    print(sol)
print(sol[max(Adapters_List)])