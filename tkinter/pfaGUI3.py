from tkinter import *
from tkinter.messagebox import showinfo,showwarning,showerror
from functools import partial as ptl

CRIT='Crit'
WARN='Warn'
INFO='Info'

SIGHS={
    'do not enter':CRIT,
    'roading crossing':INFO,
    '55/n speed limit':WARN,
    'wrong way':CRIT,
    'merging traffic':INFO,
    'one way':WARN
}

root=Tk()
root.title("traffic informantion")

critCB=lambda : showerror('Error','Error Button Pressed')
warnCB=lambda : showwarning('Warn','Warning Button Pressed')
infoCB=lambda : showinfo('Info','Information Button Pressed')


quitButton=Button(root,text='QUIT',command=root.quit,fg='green',bg='red')
quitButton.pack()

parentButton=ptl(Button,root)
CritButton=ptl(parentButton,command=critCB,fg='red',bg='white')
InfoButton=ptl(parentButton,command=warnCB,fg='black',bg='white')
WarnButton=ptl(parentButton,command=infoCB,fg='black',bg='goldenrod')

for sign in SIGHS:
    sign_value=SIGHS[sign]
    cmd='%sButton(text=%r%s).pack(fill=X,expand=YES)'%(sign_value,sign,'.upper()' if sign_value==CRIT else '.title()')
    print(cmd)
    eval(cmd)

root.mainloop()
