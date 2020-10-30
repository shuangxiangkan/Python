import tkinter

win=tkinter.Tk()
win.title("entry2")
win.geometry("400x300+20+50")

entry1=tkinter.Entry(win,show="*")
entry1.pack()

e=tkinter.Variable()
e.set("just test")

entry2=tkinter.Entry(win,textvariable=e)
entry2.pack()

print(e.get())
print(entry2.get())


win.mainloop()