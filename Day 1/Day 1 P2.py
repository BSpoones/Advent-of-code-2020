with open("Expense report.txt") as f:
    content = f.read()
    ExpenseList = content.split("\n")

ExpenseList = list(map(int,ExpenseList))

for i, num in enumerate(ExpenseList):
    firstVal = ExpenseList[i]
    for j, num in enumerate(ExpenseList):
        secondVal = ExpenseList[j]
        for k, num in enumerate(ExpenseList):
            thirdVal = ExpenseList[k]
            if firstVal+secondVal+thirdVal==2020:
                print(firstVal,secondVal,thirdVal)