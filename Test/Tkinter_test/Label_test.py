import tkinter

win=tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# Label控件：可以显示文本

# win 父窗体
# text:显示的文本内容
# bg:背景色
# fg:字体颜色
# font:字体
# wraplength:指定text文本中多宽之后换行
# justify:这是换行之后的对齐方式
# anchor:位置 n北，e东，w西，s南，center居中，还可以写在一起：ne东北方向
label=tkinter.Label(win,
                    # text="i",
                    text="i live in coastal city and it has beautiful beaches",
                    bg="pink",fg="red",
                    font=("黑体",20),
                    width=10,
                    height=7,
                    wraplength=200,
                    justify="right",
                    anchor="center")
# 显示出来
label.pack()

win.mainloop()