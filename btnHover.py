from tkinter import *

root =Tk()

def entered(e):
    btn.config(bg="white")
    status.config(text="you Hovered")

def leaved(e):
    btn.config(bg="SystemButtonFace")
    status.config(text="")


btn=Button(root,text="Click Me")
btn.pack()
btn.bind("<Enter>",entered)
btn.bind("<Leave>",leaved)
status=Label(root,text="")
status.pack(fill=X,side=BOTTOM)


root.mainloop()