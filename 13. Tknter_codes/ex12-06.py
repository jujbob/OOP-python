from tkinter import *

## 함수 선언부
def  myFunc() :
    if myVar.get() == 1 :
        label1.configure(text="벤츠")
    elif myVar.get() == 2 :
        label1.configure(text="BMW")
    else :
        label1.configure(text="아우디")

## 메인 코드부
root = Tk()
root.geometry('300x200')

myVar = IntVar()
rb1 = Radiobutton(root, text="벤츠", variable=myVar, value=1, command=myFunc)
rb1.pack()
rb2 = Radiobutton(root, text="BMW", variable=myVar, value=2, command=myFunc)
rb2.pack()
rb3 = Radiobutton(root, text="아우디", variable=myVar, value=3, command=myFunc)
rb3.pack()

label1 = Label(root, text="선택한 차량 : ", fg="red")
label1.pack()

root.mainloop()
