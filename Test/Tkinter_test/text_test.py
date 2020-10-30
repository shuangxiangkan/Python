import tkinter

win=tkinter.Tk()
win.title("text")
win.geometry("400x400+200+50")

# 文本控件：用于显示多行文本

# height表示的是显示的行数
text=tkinter.Text(win,width=50,height=10)
text.pack()

str="这几天心里颇不宁静。今晚在院子里坐着乘凉，忽然想起日日走过的荷塘，在这满月的光里，总该另有一番样子吧。月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；妻在屋里拍着闰儿⑴，迷迷糊糊地哼着眠歌。我悄悄地披了大衫，带上门出去。"

# INSERT表示输入光标所在的位置，初始化后的输入光标默认在左上角
text.insert(tkinter.INSERT,str)
text.insert(tkinter.END,"at the end.")


win.mainloop()
