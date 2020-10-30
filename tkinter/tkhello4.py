from tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top=Tk()
top.geometry('250x150')

label=Label(top,text='Hello World!',font='Helvetica -12 bold')
label.pack(fill=Y,expand=YES)

scale=Scale(top,from_=0,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=YES)

quit=Button(top,text="QUIT",command=top.quit,foreground='green',background='red')
quit.pack()




top.mainloop()

