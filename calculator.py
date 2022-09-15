from tkinter import *

root=Tk()

root.geometry("800x800")

scvalue=StringVar()
scvalue.set("")

screen=Entry(root,textvar=scvalue,font="aero 20 bold",justify=RIGHT,bd=5,bg="skyblue",width=640)
screen.pack(anchor="e")


f=Frame(root,width=100,height=10,bg="grey",padx=50)
f2=Frame(root,width=100,height=10,bg="grey",padx=50)
f3=Frame(root,width=100,height=10,bg="grey",padx=50)
f4=Frame(root,width=100,height=10,bg="grey",padx=50)
f5=Frame(root,bg="grey",width=320,height=100,padx=50)
f6=Frame(root,bg="grey",width=320,height=100,padx=50)
f7=Frame(root,bg="grey",width=320,height=100,padx=50)
    
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print (text)
    if text=="=":
        if scvalue.get().isdigit():
                value=int(scvalue.get())
        else :
                try:
                        value=eval(scvalue.get())
                except Exception as e:
                        value="SYNTAX ERROR"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue. get()+text)
        screen.update()            
    
Numerals="1234567890+-/*%=C."
Actions="00"
btn=[]
i=0
l=0

for k in range (0,3):
        btn.append(Button(f,text=Numerals[i],font="aero 15 bold",padx=12,pady=10,bg="royalblue",activebackground="skyblue"))
        btn[i].pack(fill=X,side=LEFT,anchor="n",padx=10,pady=5)
        btn[i].bind("<Button-1>",click)
        i+=1
        f.pack()
for k in range (0,3):
        btn.append(Button(f2,text=Numerals[i],font="aero 15 bold",padx=10,pady=10,bg="royalblue",activebackground="skyblue"))
        btn[i].pack(fill=X,side='left',anchor="n",padx=10,pady=5)
        btn[i].bind("<Button-1>",click)
        i+=1
        f2.pack()
        
for k in range (0,3):
        btn.append(Button(f3,text=Numerals[i],font="aero 15 bold",padx=10,pady=10,bg="royalblue",activebackground="skyblue"))
        btn[i].pack(fill=X,side=LEFT,anchor="n",padx=10,pady=5)
        btn[i].bind("<Button-1>",click)
        i+=1
        f3.pack()
        
for k in range (0,3):
        btn.append(Button(f4,text=Numerals[i],font="aero 15 bold",padx=10,pady=10,bg="royalblue",activebackground="skyblue"))
        btn[i].pack(fill=X,side=LEFT,anchor="n",padx=10,pady=5)
        btn[i].bind("<Button-1>",click)
        i+=1
        f4.pack()

for k in range (0,3):
        btn.append(Button(f5,text=Numerals[i],font="aero 15 bold",padx=10,pady=10,bg="royalblue",activebackground="skyblue"))
        btn[i].pack(fill=X,side=LEFT,padx=10,pady=5,anchor="n")
        btn[i].bind("<Button-1>",click)
        i+=1
        f5.pack(side=TOP)
        
for k in range (0,3):
        btn.append(Button(f6,text=Numerals[i],font="aero 15 bold",padx=10,pady=10,bg="royalblue",activebackground="skyblue"))
        btn[i].pack(fill=X,side=LEFT,padx=10,pady=5,anchor="n")
        btn[i].bind("<Button-1>",click)
        i+=1
        f6.pack(side=TOP)

btn.append(Button(f7,text="00",font="aero 15 bold",padx=25,pady=10,bg="royalblue",activebackground="skyblue"))
btn[i].pack(fill=X,side=LEFT,padx=55,pady=5,anchor="n")
btn[i].bind("<Button-1>",click)
i+=1
f7.pack(side=TOP)
        

    
root.mainloop()