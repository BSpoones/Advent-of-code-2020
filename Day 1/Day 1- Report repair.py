with open("Expense report.txt") as f:
    content = f.read()
    ExpenseList = content.split("\n")

ExpenseList = list(map(int,ExpenseList))
combinations = []
for i, num in enumerate(ExpenseList):
    newVal = 2020-num#ExpenseList[i]
    if newVal in ExpenseList:
        print("One of the combinations is",newVal)
        combinations.append(newVal)
    
print("The product of the two combinations is",combinations[0]*combinations[1])