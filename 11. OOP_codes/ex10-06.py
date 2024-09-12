class Rabbit :   
    shape = "" 
    xPos = 0   
    yPos = 0   
    def goto(self, x, y) :
        self.xPos = x
        self.yPos = y


class HouseRabbit(Rabbit) :
    owner = ""
    def eatFeed() :
        print("집토끼가 모이를 먹습니다")


class MountineRabbit(Rabbit) :
    mountine = ""
    def eatWildglass() :
        print("산토끼가 들풀을 먹습니다")
