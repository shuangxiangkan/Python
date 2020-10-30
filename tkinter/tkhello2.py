import tkinter

top=tkinter.Tk()
quit1=tkinter.Button(top,text='hello!',command=top.quit)
quit1.pack(padx=100,pady=50,ipady=10)
quit2=tkinter.Button(top,text='world!',command=top.quit)
quit2.pack(padx=100,pady=50,ipady=10)
tkinter.mainloop()