from tkinter import *
from tkinter.filedialog  import *

root = Tk()
root.geometry('200x200')

label1 = Label(root, text="선택된 파일이름")
label1.pack()

savefname = asksaveasfilename(parent=root,  filetypes=(("JPG 파일", "*.jpg"),  ("모든 파일", "*.*") ))
label1.configure(text=savefname)

root.mainloop()
