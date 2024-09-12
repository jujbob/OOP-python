import turtle
import random
from tkinter.filedialog  import *
from tkinter.simpledialog  import *

root = Tk()

shape = askstring("모양", "거북이 모양 : turtle, circle, triangle 등")
color = askstring("색상", "거북이 색상 : red, green, magenta 등")
size = askinteger("크기", "거북이 크기(1~10)", minvalue=1, maxvalue=10)
repeat = askinteger("반복", "거북이가 그릴 원의 개수")

root.destroy()


turtle.shape(shape)
turtle.pencolor(color)
turtle.turtlesize(size,size,size)

turtle.setup(850, 850)
turtle.screensize(800, 800)


for i in range(repeat) :
    turtle.circle(i*10)

turtle.done()
