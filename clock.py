import time
from tkinter import *
root =Tk()

def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    am=time.strftime("%p")
    l1.config(text=hour+ ":"+ minute+ ":"+second+" "+ am)
    l1.after(1000,clock)
f1=Frame (root,width=500,height=200)
f1.pack()
l1=Label(f1,text="",font="AERO 55 bold",bg='black',fg='red')
l1.pack()

clock()

root.mainloop()