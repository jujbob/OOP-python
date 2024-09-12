inFile = None 
inList = []    

inFile = open("C:/FirstPython/Chapter09/myData1.txt", "r", encoding="UTF-8")

inList = inFile.readlines()
print(inList)

inFile.close()
