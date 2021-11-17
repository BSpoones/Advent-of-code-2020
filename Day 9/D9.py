
with open("Numbers.txt") as f:
    content = f.read()
    Number_List = content.split("\n")

Number_List = [int(Number_List[i]) for i in range(len(Number_List))]

for i, val in enumerate(Number_List,start=25):
    hasMatch = False
    if i >999: break

    Number_Fragment = (Number_List[i-25:i])
    expected = (Number_List[i])
    for j in Number_Fragment:
        for k in Number_Fragment:
            if j+k == expected and j!=k:
                print(j,k,expected)
                hasMatch = True
    if hasMatch == False:

        print("Part 1:",expected)
        break

#Part 2
"""
Need to find continuous set of numbers to equal expected
For loop to choose first number, check if < expected, if not then add the next number. 
Continue doing until number > or == expected 
Expected = 466456641
"""

    
for i, number in enumerate(Number_List):
    position = i
    total = 0
    Numbers = []
    while sum(Numbers)<= expected:
        Numbers.append(Number_List[position])
        position +=1
        if sum(Numbers) == expected:
            print(len(Numbers))
            print(min(Numbers)+max(Numbers))
