with open("Passwords.txt") as f:
    content = f.read()
    PasswordList = content.split("\n")

PassCount = 0
def checkPassword(MinNum, MaxNum, key, content):
    global PassCount
    count = int(content.count(key))
    if count <= int(MaxNum) and count >= int(MinNum):
        PassCount +=1


for password in PasswordList:
    dashPos=(password.find('-'))
    colonPos=(password.find(':'))
    if dashPos == 1:
        MinNum = (password[0:1])
    elif dashPos ==2:
        MinNum = (password[0:2])
    if password[dashPos+2] == " ":
        MaxNum = password[dashPos+1]
    elif password[dashPos+2] != " ":
        MaxNum = password[dashPos+1:dashPos+3]
    key = password[colonPos-1]
    content = password[colonPos+2:]
    checkPassword(MinNum,MaxNum,key,content)

print(PassCount)