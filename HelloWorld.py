import tkinter.messagebox as mbox 
import tkinter as tk

class HelloWorld(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.winfo_toplevel().title("")
        self.grid()
        self.btns = tk.StringVar()
        self.createField()
        self.boxSize = '50'
        self.toggle = True

    def createField(self):
        self.createButton(0,0,1)

    def createButton(self,xpos,ypos,id):
        self.button = tk.Button(self, text="click here.",height=2,width=10, font=('Helvetica', '50'), command=lambda: self.updateButtonText(id))
        self.button.grid(row=xpos,column=ypos)

    def updateButtonText(self,id):
        s = int(self.boxSize)+10
        self.boxSize = str(s)
        if self.toggle:
            self.button.config(text="Hello World",font=('Helvetica', self.boxSize))
            self.toggle = False
        else:
            self.button.config(text="click again!",font=('Helvetica', self.boxSize))
            self.toggle = True

hw = HelloWorld()
hw.mainloop()