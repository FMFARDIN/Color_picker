from tkinter import *
from tkinter import colorchooser
import pyperclip
root = Tk()
root.geometry("400x300")
root.iconbitmap("color_picker.ico")
root.title(" Simple Color Picker")
def color():    
    color = colorchooser.askcolor()[1]
    label = Label(root, text=color).pack()
    pyperclip.copy(color)   

text = Label(root, text="Choose a color it will be copied to your clipboard automatically", fg="#828282").pack()
btn = Button(root, text="Choose a color",bg="#0091ff",activebackground="#00aeff",borderwidth="10", bd=0, font="Ubuntu", command=color).pack(pady="100",padx="90")


mainloop()