from calendar import month
from tkcalendar import *
from tkinter import *

root=Tk()
f1=Frame(root,width=400,height=400)
my_cal=Calendar(f1,selectmode="day",month=1,year=2021,day=21)
my_cal.pack(fill=BOTH,expand=1)
f1.pack()

def update():
    l1.config(text=my_cal.get_date())
        


b1=Button(root,text="det",command=update)
b1.pack()
l1=Label(root,text="")
l1.pack()
root.mainloop()

