from tkinter import *
from tkinter import filedialog

class FiledialogTest():
    def __init__(self):
        self.root=Tk()
        self.root.title("filedialog")



        self.frame=Frame(self.root)
        self.frame.pack()

        self.string=StringVar(self.root)
        self.string.set("请选择文件")


        self.entry=Entry(self.frame,textvariable=self.string)
        self.entry.pack(side=LEFT,fill=X,expand=YES)

        self.select=Button(self.frame,text="select file",command=self.file_select)
        self.select.pack(side=LEFT)

        self.root.mainloop()

    def file_select(self):
        fileName=filedialog.askopenfilename(title="选择python文件",filetypes=[("python文件","*.py")],initialdir="d:/")
        self.string.set(fileName)

if __name__ == '__main__':
    f=FiledialogTest()