from tkinter import *

# 함수 정의 부분
def clickMouse(event) :
    if event.num ==1 :
        txt = "왼쪽 버튼 :  (" + str(event.y) + "," + str(event.x) + ")"
    elif event.num == 3 :
        txt = "오른쪽 버튼 :  (" + str(event.y) + "," + str(event.x) + ")"

    label1.configure(text=txt)

# 메인 코드 부분
root = Tk()
root.geometry("400x400")

label1 = Label(root, text="여기가 바뀝니다.", fg="red" )
label1.pack( expand=1, anchor=CENTER)

root.bind("<Button>",clickMouse)

root.mainloop()
