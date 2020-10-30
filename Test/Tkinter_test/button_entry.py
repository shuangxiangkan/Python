import tkinter

win=tkinter.Tk()
win.title("button_entry")
win.geometry("400x400+200+50")

def showinfo():
    # 获取输入的内容
    print(entry.get())

entry=tkinter.Entry(win)
entry.pack()

button=tkinter.Button(win,text="按钮",command=showinfo)
button.pack()

win.mainloop()