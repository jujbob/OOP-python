inFile = None  # 입력 파일
inStr = ""      # 읽어온 문자열
 
inFile = open("C:/FirstPython/Chapter09/myData1.txt", "r", encoding="UTF-8")

inStr = inFile.readline()
print(inStr, end="")

inStr = inFile.readline()
print(inStr, end="")

inStr = inFile.readline()
print(inStr, end="")

inFile.close()
