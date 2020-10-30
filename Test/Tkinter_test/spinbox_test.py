import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")





v = tkinter.StringVar()

def updata():
    print(v.get())



sp = tkinter.Spinbox(win, from_=0, to=100, increment=5,textvariable=v, command=updata)
# sp = tkinter.Spinbox(win, values=(0,2,4,6,8))
sp.pack()

# 赋值
v.set(20)
# 取值
print(v.get())

win.mainloop()