#1
## 클래스 선언
class Line:
    length = 0
    color = ""
    def __init__(self, length) :
        self.length = length
        print(self.length, '길이의 선이 생성되었습니다.')

#2
    def __del__(self) :
        print(self.length, '길이의 선이 제거되었습니다.')

#3
    def __add__(self, other):
        return self.length + other.length

#4
    def __lt__(self, other) :
        return self.length < other.length

#5
    def __eq__(self, other) :
        return self.length == other.length

#6
## 메인 코드 부분
line1 = Line(10)
line2 = Line(5)

#7
print('두 선의 합 : ', line1 + line2)

#8
if line1 < line2 :
    print('선2가 더 깁니다.')
    del(line1)
    
elif line1 == line2 :
    print('두 선이 같네요')

else :
    print('선1이 더 깁니다.')
    del(line2)
