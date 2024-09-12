#1
from tkinter import *

#2
# 함수 선언부
def clickLeft(e) :
    canvas.create_oval(e.x-20, e.y-20, e.x+20, e.y+20, width=5, outline="green")

#3
def clickRight(e) :
    canvas.create_rectangle(e.x-20, e.y-20, e.x+20, e.y+20, width=5, outline="red")

#4
# 메인 코드부
root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()

#5
canvas.bind("<Button-1>", clickLeft)
canvas.bind("<Button-3>", clickRight)

root.mainloop()
