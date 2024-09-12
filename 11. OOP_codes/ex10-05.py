class Rabbit :
    shape = ""
    def __add__( self, other ) :
        print("객체", self.shape,"와", other.shape, "가 친구가 되었습니다.")

rabbit1 = Rabbit()
rabbit1.shape = "엽기토끼"
rabbit2 = Rabbit()
rabbit2.shape = "도비"

rabbit1+rabbit2
