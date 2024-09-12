inFile = None 
inList = [ ]
inStr = ""

inFile = open("C:/FirstPython/Chapter09/myData1.txt", "r", encoding="UTF-8")

inList = inFile.readlines()
for inStr in inList :
    print(inStr, end="")

inFile.close()
