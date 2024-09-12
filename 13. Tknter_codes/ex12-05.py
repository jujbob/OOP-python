from tkinter import *
from tkinter import messagebox

## 함수 선언부
def  myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼 OFF 네요.")
    else :
        messagebox.showinfo("", "체크버튼 ON 이네요.")

## 메인 코드부
root = Tk()
root.geometry('300x100')

chk = IntVar()
cb1 = Checkbutton(root, text="클릭하세요", variable=chk, command=myFunc)
cb1.pack()

root.mainloop()
