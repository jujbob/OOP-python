outFile = None 
outStr = ""

outFile=open("c:/FirstPython/Chapter09/myData2.txt", "w")

outStr = "안녕하세요?"
outFile.writelines(outStr+"\n")

outStr = "반갑습니다."
outFile.writelines(outStr+"\n")

outStr = "자주만나요. ^^"
outFile.writelines(outStr+"\n")

outFile.close()
print("--- myData2.txt 파일이 저장됨 ---")
