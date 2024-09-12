#1
import turtle
## 클래스 및 함수 선언부
class SeaTurtle(turtle.Turtle) :
    name = ''
    body = None
    def __init__(self) :
        self.body = turtle.Turtle('triangle')
        self.body.color("blue")
        self.name = "바다 거북"
    def swim(self, x, y) :
        self.body.goto(x, y)

#2
class SandTurtle(turtle.Turtle) :
    name = ''
    body = None
    def __init__(self) :
        self.body = turtle.Turtle('circle')
        self.body.color("red")
        self.name = "모래 거북"
    def walk(self, x, y) :
        self.body.goto(x, y)

#3
## 전역 변수 선언부
seaTut, sandTut = None, None

#4
# 메인 코드
seaTut = SeaTurtle()
sandTut = SandTurtle()

#5
seaTut.swim(100, 100)
seaTut.body.write(seaTut.name, font=("Arial", 20))

sandTut.walk(-100, 100)
sandTut.body.write(sandTut.name, font=("Arial", 20))
