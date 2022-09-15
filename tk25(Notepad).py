from posixpath import basename
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "- Notepad")
        TextArea.delete(1.0,END)
        text=open(file,"r")
        TextArea.insert(1.0,text.read())
        text.close()
    
def savefile():
    global file
    if file ==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            #save as new file
            text=open(file,"w")
            text.write(TextArea.get(1.0,END))
            text.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("saved")
    else:
        text=open(file,"w")
        text.write(TextArea.get(1.0,END))
        text.close()
        
def cut():
    TextArea.event_generate(("<<Cut>>"))
    
def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
    
def quitapp():
    root.destroy()

def about():
    showinfo("ABOUT US","Created By R&Company")
       


if __name__ == '__main__':
    root =Tk()
    root.title("Untitled - Notepad")
    root.geometry("720x720")
    
    
    #Text area
    TextArea=Text(root,font="lucida 12")
    file=None
    TextArea.pack(expand=True,fill=BOTH )
    
    #menubar
    Menubar=Menu(root)
    
    #File Menu
    Filemenu=Menu(Menubar,tearoff=0)
    Filemenu.add_command(label="New",command =newfile)
    Filemenu.add_command(label="Open",command =openfile)
    Filemenu.add_command(label="Save",command =savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command =quitapp)
    Menubar.add_cascade(label="File",menu=Filemenu)
    root.config(menu=Menubar)
    
    #Edit MEnu
    
    Editmenu=Menu(Menubar,tearoff=0)
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=Editmenu)
    root.config(menu=Menubar)
    
    #helpmenu
    
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    root.config(menu=Menubar)
    
    scroll=Scrollbar(TextArea)
    scroll.pack(fill=Y,side=RIGHT)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    
    
root.mainloop()