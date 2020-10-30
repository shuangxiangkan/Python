from tkinter import *

def resize(ev=None):
    print(scale.get())
    label.config(font="Helvetica -%d bold"%scale.get())
    return None



top=Tk()
top.geometry("600x400")

label=Label(top,text="Hello World!",font="Helvetica -121 bold")
label.pack(fill=Y,expand=1)

scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit=Button(top,text="Quit",command=top.quit,activeforeground="yellow",activebackground="green")
quit.pack()

mainloop()
