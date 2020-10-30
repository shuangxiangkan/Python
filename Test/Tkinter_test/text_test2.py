import tkinter

win=tkinter.Tk()
win.title("my_text_test")
win.geometry("600x300+300+300")

my_text=tkinter.Text(win,width=30,height=10)
my_text.pack()
str="这几天心里颇不宁静。今晚在院子里坐着乘凉，忽然想起日日走过的荷塘，在这满月的光里，总该另有一番样子吧。月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；妻在屋里拍着闰儿⑴，迷迷糊糊地哼着眠歌。我悄悄地披了大衫，带上门出去。"
my_text.insert(tkinter.INSERT,str)

win.mainloop()