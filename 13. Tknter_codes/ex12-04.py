from tkinter import *
from tkinter import messagebox

## 함수 선언부

def myFunc() :
    messagebox.showinfo("버튼 클릭", "버튼을 눌렀군요 ^^")

## 메인 코드부
root = Tk()
root.geometry('300x100')

button1 = Button(root, text='클릭하세요', fg='red', command=myFunc)
button1.pack()

root.mainloop()
