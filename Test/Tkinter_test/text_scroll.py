import tkinter

win=tkinter.Tk()
win.title("scroll_test")
win.geometry("400x100+200+50")

# 创建滚动条
scroll=tkinter.Scrollbar()

text=tkinter.Text(win,width=30,height=10)
# side放到窗体的哪一侧，fill填充
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack()

str="这几天心里颇不宁静。今晚在院子里坐着乘凉，忽然想起日日走过的荷塘，在这满月的光里，总该另有一番样子吧。月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；妻在屋里拍着闰儿⑴，迷迷糊糊地哼着眠歌。我悄悄地披了大衫，带上门出去。"

text.insert(tkinter.INSERT,str)

win.mainloop()