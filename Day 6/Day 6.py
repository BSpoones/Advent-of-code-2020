with open("Form Responses.txt") as f:
    content = f.read()
    ResponseList = content.split("\n\n")
    ResponseList = [item.replace("\n","") for item in ResponseList]

Count = 0
for item in ResponseList:
    Unique = []
    for char in item:
        if char not in Unique:
            Unique.append(char)
    Count += len(Unique)
print("Part 1:",Count)


NewResponseList = content.split("\n\n")
ResponseArray = [item.split("\n") for item in NewResponseList]
Count2 = 0
for i, lst in enumerate(ResponseArray):
    for j, item in enumerate(lst):
            item = ''.join(sorted(item))
            ResponseArray[i][j] = item
    links = (set.intersection(*map(set,lst)))
    Count2 += len(links)

print("Part 2:",Count2)
