import tkinter


win=tkinter.Tk()
win.title("mouse_click")
win.geometry("400x400+200+50")

# <Key> 响应所有的按键（要有焦点）

label=tkinter.Label(win,text="***********8",bg="red")

# 设置焦点
label.focus_get()
label.pack()

def func(event):
    print("event.char=",event.char)
    print("event.keycode=",event.keycode)

label.bind("<Key>",func)

win.mainloop()