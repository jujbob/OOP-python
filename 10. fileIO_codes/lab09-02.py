#1
inFile, outFile = None, None 
inStr = ""

inFile=open("C:/FirstPython/Chapter09/pythonNote.txt", "r", encoding="UTF-8")
outFile=open("C:/FirstPython/Chapter09/myNote.txt", "w")

#2
inList = inFile.readlines()
for inStr in inList :
    outFile.writelines(inStr)

#3
inFile.close()
outFile.close()
print("--- pythonNote.txt가 newFile.txt로 복사되었음 ---")
