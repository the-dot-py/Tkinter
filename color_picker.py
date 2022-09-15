from tkinter import *
from tkinter import colorchooser

root=Tk()

def choose():
    color=colorchooser.askcolor()[1]
    l1=Label(root,text="THIS IS THE COLOR",bg=color)
    l1.pack(pady=20,ipadx=10,fill=BOTH,ipady=20)
    btn["bg"]=color
    # btn["font"]="HELVETICA 22"

btn=Button(root,text="Choose a Color",font="Amaze 33",command=choose)
btn.pack()

root.mainloop()