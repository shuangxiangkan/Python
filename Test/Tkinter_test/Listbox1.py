import tkinter

win=tkinter.Tk()
win.title("Listbox1")
win.geometry("400x400+200+50")

# 列表框控件，可以包含一个或多个文本框
lb=tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()

for item in ["good","nice","handsome","aaa","bbb","ccc","ddd"]:
    # 按顺序添加
    lb.insert(tkinter.END,item)

# 在开始添加
lb.insert(tkinter.ACTIVE,"cool")

# 返回当前的索引项，不是item元素
# print(lb.curselection())

#获取列表中的元素个数
print(lb.size())

win.mainloop()
