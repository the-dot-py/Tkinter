from tkinter import *

root=Tk()

w=400
h=400
x=w//2
y=h//2

my_canvas=Canvas(root,width=800,height=400,bg="white")
my_canvas.pack()

# oval=my_canvas.create_oval(x,y,x+10,y+10,fill="red")

def left(event):
    x=-10
    y=0
    my_canvas.move(oval,x,y)
def right(event):
    x=10
    y=0
    my_canvas.move(oval,x,y)
def up(event):
    x=0
    y=-10
    my_canvas.move(oval,x,y)
def down(event):
    x=0
    y=10
    my_canvas.move(oval,x,y)

def move(event):
    global img ,my_img  
    img=PhotoImage(file="myimages/DOB.PNG")
    my_img=my_canvas.create_image(event.x,event.y,image=img)
 
# root.bind("<Left>",left)
# root.bind("<Right>",right)
# root.bind("<Up>",up)
# root.bind("<Down>",down)

root.bind("<B1-Motion>",move)

root.mainloop()