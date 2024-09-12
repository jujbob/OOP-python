from tkinter import *
root = Tk()

# 함수 정의 부분

canvas = Canvas(root, 
height=400, 
width=400)
canvas.pack()

# 메인 코드 부분
canvas.create_line(150, 150, 250, 250, width=5, fill="red")
canvas.create_oval(50, 50, 150, 150, outline="green")
canvas.create_rectangle(300, 300, 350, 350, width=10, outline="blue", fill="yellow")

root.mainloop()
