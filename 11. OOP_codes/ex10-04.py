class  Rabbit :
    shape = ""
    def __del__( self ) :
        print("이제", self.shape,"는 자유에요~~")

rabbit = Rabbit()
rabbit.shape = "도비"
del(rabbit)
