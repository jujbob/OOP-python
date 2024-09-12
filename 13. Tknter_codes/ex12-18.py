from tkinter import *
from tkinter.simpledialog import *

root = Tk()
root.geometry('200x200')

label1 = Label(root, text="입력된 값")
label1.pack()

value = askinteger("숫자입력", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)
label1.configure(text=str(value))

root.mainloop()
