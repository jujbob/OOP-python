class Rabbit :
    shape = "" # 토끼 모양
    xPos = 0   # X 위치
    yPos = 0   # Y 위치

    def goto(self, x, y) :
        self.xPos = x
        self.yPos = y
