#1
## 클래스 및 함수 선언부
class Rabbit :
    shape = "" # 토끼 모양
    xPos = 0   # X 위치
    yPos = 0   # Y 위치

    def goto(self, x, y) :
        self.xPos = x
        self.yPos = y

#2
## 전역 변수 선언부
rabbit = None
userX, userY = 0, 0

#3
## 메인 코드
rabbit = Rabbit()

rabbit.shape = "토끼"

#4
while True :
    userX = int(input("토끼가 이동할  X좌표 ==>"))
    userY = int(input("토끼가 이동할  Y좌표 ==>"))

    rabbit.goto(userX, userY)

    print("**토끼의 현재 위치는 (", str(userX), ",", str(userY), ")") 
