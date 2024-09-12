inFile = None 
inStr = ""     

inFile = open("C:/FirstPython/Chapter09/myData1.txt", "r", encoding="UTF-8")

while True :
    inStr = inFile.readline()
    if inStr == "" :
        break
    print(inStr, end="")

inFile.close()
