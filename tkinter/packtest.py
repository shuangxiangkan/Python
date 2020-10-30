from tkinter import *

root=Tk()
root.geometry('400x300')

Button(root,text= "A",bg='red').pack(side = LEFT, expand = YES, fill = Y)
Button(root,text= "B").pack(side = TOP, expand = NO, fill = X)
Button(root,text= "C",bg='green').pack(side = RIGHT, expand = YES, fill = BOTH,anchor=NE)
Button(root,text= "E").pack(side = TOP, expand = YES, fill = BOTH)
Button(root,text= "D").pack(side = LEFT, expand = YES, fill = Y)




root.mainloop()