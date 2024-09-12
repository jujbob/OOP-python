from tkinter import *
root = Tk()

label1 = Label(root, text="난생처음~~ Python을")
label1.pack()
label2 = Label(root, text="열심히", font=("궁서체", 30), fg="red")
label2.pack()
label3 = Label(root, text="코딩 중입니다.", bg="yellow", width=20, height=5, anchor=CENTER)
label3.pack()

root.mainloop()
