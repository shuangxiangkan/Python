import tkinter

win=tkinter.Tk()
win.title("absolute_layout")
win.geometry("800x600+200+50")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="nice",bg="red")
label3=tkinter.Label(win,text="excellent",bg="green")

# 绝对布局，窗口的变化对位置有影响
label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)
label3.pack()

win.mainloop()