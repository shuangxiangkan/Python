import tkinter

win=tkinter.Tk()
win.title("Listbox2")
win.geometry("400x400+200+50")

# 绑定变量
lbv=tkinter.StringVar()

# 与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb=tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()

for item in ['good','nice','handsome','aaa','bbb','ccc']:
    #按顺序添加
    lb.insert(tkinter.END,item)

# 打印当前列表中的选型
print(lbv.get())

# 绑定事件
def myprint(event):
    print(lb.get(lb.curselection()))

lb.bind("<Double-Button-1>",myprint)

win.mainloop()

win.mainloop()
