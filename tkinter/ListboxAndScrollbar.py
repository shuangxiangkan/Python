from tkinter import *
import os

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("listbox and scrollbar")

        self.string=StringVar(self.root)

        self.label=Label(self.root,textvariable=self.string)
        self.label.pack()

        self.frame1=Frame(self.root)
        self.frame1.pack()

        self.scrollbar = Scrollbar(self.frame1)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.frame1, width=50)
        self.initDir()
        self.listbox.bind("<Double-1>", self.listboxClic)
        # self.listbox.bind("<Button-1>",self.listboxClic)
        self.listbox.pack()

        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry=Entry(self.root,textvariable=self.string)
        self.entry.pack(fill=X)

        self.frame2=Frame(self.root)
        self.frame2.pack()

        self.clear=Button(self.frame2,text='Clear',command=self.clearEntry)
        self.clear.pack(side=LEFT)

        self.listDir=Button(self.frame2,text='listDirectory')
        self.listDir.pack(side=LEFT)

        self.Quit=Button(self.frame2,text="Quit",command=self.root.quit)
        self.Quit.pack(side=LEFT)


        self.root.mainloop()

    def initDir(self):
        dirItems=os.listdir(os.curdir)
        self.listbox.delete(0,END)
        self.listbox.insert(END,os.pardir)
        for item in dirItems:
            self.listbox.insert(END,item)
        # 提前选定第一项
        self.listbox.select_set(0)
        self.string.set(os.getcwd())

    def clearEntry(self):
        self.string.set('')

    def listboxClic(self,event):

        selectedItem=self.listbox.get(self.listbox.curselection())

        if not os.path.isdir(selectedItem):
            error=selectedItem+"不是目录"
            self.string.set(error)
            return
        os.chdir(selectedItem)
        self.initDir()







if __name__ == '__main__':
    a=App()
