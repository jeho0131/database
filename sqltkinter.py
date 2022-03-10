from tkinter import *
from tkinter import messagebox

def clickButton() :
    messagebox.showinfo('버튼 클릭', '버튼을 눌렀습니다..')

root = Tk()
root.geometry("200x250")

upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width = 10)
editBox.pack(padx = 20, pady = 20)

listbox = Listbox(downFrame, bg='yellow')
listbox.pack()

listbox.insert(END, "하나")
listbox.insert(END, "둘")
listbox.insert(END, "셋")

root.mainloop()
