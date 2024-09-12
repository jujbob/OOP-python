#1
secureFile = None
inStr, secure = "", ""

secureFile=open("C:/FirstPython/Chapter09/secure.txt", "w", encoding="UTF-8")

#2
while True :
    inStr = input('스파이에게 전달할 메시지 ==>')
    if inStr == "" :
        break

#3    
    for ch in inStr :
        num = ord(ch)
        num += 100
        secure += chr(num)

#4
    secureFile.writelines(secure)

secureFile.close()
print('--- secure.txt 암호화 완료 ---')
