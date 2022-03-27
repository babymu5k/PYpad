from cProfile import label
import tkinter
import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter as tk
import platform
import time


# Create object
splash_root = Tk()
   
# Adjust size
splash_root.geometry("300x100")
 
# Set Label
splash_label = Label(splash_root,text="PYpad V0.1.5\nMade By SuperPythonGuy\nUNDER DEVELOPMENT\nLOADING....",font=20)
splash_label.pack()
 
# main window function
def main(): 
    # destroy splash window
    splash_root.destroy()
         
# Set Interval
splash_root.after(1250,main)
 
 # Execute tkinter
mainloop()

#Computer network name
a={platform.node()}
#Machine type
b={platform.machine()}
#Processor type
c={platform.processor()}
#Platform type
d={platform.platform()}
#Operating system
e={platform.system()}
#Operating system release
f={platform.release()}
#Operating system version
g={platform.version()}



class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 900
    __thisHeight = 400
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None
    __thisEditMenu = Menu(__root)
    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
        		self.__root.wm_iconbitmap("notepad.ico")
        except:
        		pass

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("Untitled* - PYpad")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the text area auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)
        
        self.__thisFileMenu.add_command(label="New",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut",command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy",command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About PYpad",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)
        self.__thisHelpMenu.add_command(label="Github",command=self.__Socials)
        self.__thisHelpMenu.add_command(label="CPU Info(for fun)",command=self.__showcpu)
        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        
    
    def __quitApplication(self):
        self.__root.destroy()
        #exit()
        
    def __showAbout(self):
        showinfo("PYpad","Created by:SuperPythonGuy\nV0.1.5 Under Development")
        
    def __Socials(self):
        showinfo("Github","https://github.com/superpythonguy")
        
    def __showcpu(self):
        showinfo("info",a)
        showinfo("info",b)
        showinfo("info",c)
        showinfo("info",d)
        showinfo("info",e)        
        showinfo("info",f)
        showinfo("info",g)    


    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - PYpad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled* - PYpad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - PYpad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.__root.mainloop()

##############################################################
#Themes
##############################################################
  
##############################################################


#run main application
notepad = Notepad(width=600,height=600)
notepad.run()