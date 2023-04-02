from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElements:
    
    def __int__(self):
        print("This is CreatElement class")
        
    def createNewElement(self):
            label = Label(root,text="Anew label is been created using class",fg="red")
            label.pack()
            btn = Button(root,text = " Button ",command = self.message)
            btn.pack(padx=20,pady = 10)
            
    def message(self):
            messagebox.showinfo("showinfo","You clicked the button created using class")
                
obj_of_createElements = CreateElements()

btn= Button(root,text="click the creat lable and button element",command =obj_of_createElements.createNewElement)
btn.pack(padx=20, pady = 10)

root.mainloop()