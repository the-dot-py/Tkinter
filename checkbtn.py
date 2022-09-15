from tkinter import *


root =Tk()
var=IntVar()


def show(val):
    label=Label(root,text=val).pack()

ans=Checkbutton(root,text="Switch On/Off",variable=var).pack()
btn=Button(root,text="choose",command=lambda: show(var.get()),activebackground="Blue",width=30).pack()
root.mainloop()