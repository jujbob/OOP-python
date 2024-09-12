class Rabbit :
    shape = "" # 토끼 모양
    xPos = 0   # X 위치
    yPos = 0   # Y 위치

    def __init__(self, value) :
        self.shape = value

    def goto(self, x, y) :
        self.xPos = x
        self.yPos = y

rabbit1 = Rabbit('원')
print('rabbit1의 모양: ', rabbit1.shape)

rabbit2 = Rabbit('삼각형')
print('rabbit2의 모양: ', rabbit2.shape)

rabbit3 = Rabbit('토끼')
print('rabbit3의 모양: ', rabbit3.shape)
