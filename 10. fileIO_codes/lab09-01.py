#1
inFile = None
inStr = ""
lineNum = 1

inFile = open("C:/FirstPython/Chapter09/myData1.txt", "r", encoding="UTF-8")

#2
while True :
    inStr = inFile.readline()
    if inStr == "" :
        break
    print(lineNum, " : " , inStr, end="")
    lineNum += 1

inFile.close()
