import tkinter

win=tkinter.Tk()
win.title("my_checkbutton")
win.geometry("400x300+50+50")

def update():
    message="123"
    if hobby1.get():
        message+="money\n"
    if hobby2.get():
        message+="power\n"
    if hobby3.get():
        message+="dream\n"

    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)
    print(message)



hobby1=tkinter.BooleanVar()
check1=tkinter.Checkbutton(win,text="money",variable=hobby1,command=update)
check1.pack()
hobby2=tkinter.BooleanVar()
check2=tkinter.Checkbutton(win,text="power",variable=hobby2,command=update)
check2.pack()
hobby3=tkinter.BooleanVar()
check3=tkinter.Checkbutton(win,text="dream",variable=hobby3,command=update)
check3.pack()

text=tkinter.Text(win,width=50,height=10)
text.pack()



win.mainloop()