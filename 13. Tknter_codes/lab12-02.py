#1
from tkinter import *
from tkinter.filedialog  import *
from tkinter.simpledialog  import *

#2
root = Tk()
root.geometry('200x200')

label1 = Label(root, text="선택된 파일이름")
label1.pack()

#3
extName = askstring("확장명", "확장명을 입력(예: hwp,png,zip 등)")

#4
filename = askopenfilename(parent=root, filetypes=(("입력 파일", "*."+extName),  ("모든 파일", "*.*") ))
label1.configure(text=str(filename))

root.mainloop()
