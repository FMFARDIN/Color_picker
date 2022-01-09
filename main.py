from tkinter import *
from tkinter import colorchooser
import pyperclip

# Window attributes
root = Tk()
root.iconbitmap("color_picker.ico")
root.title(" Simple Color Picker")

# Function
def color():    
    color = colorchooser.askcolor()[1]
    label = Label(root, text=color, bg=color, font="Ubuntu, 12").pack(padx=5,pady=10)
    pyperclip.copy(color)   

# Upper text
text = Label(root, text="Choose a color it will be copied to your clipboard automatically", fg="#828282").pack(pady=10,padx=10)

# Choose color button
btn = Button(root, text="Choose a color",bg="#0091ff",activebackground="#00aeff",borderwidth="10", bd=0, font="Ubuntu", command=color).pack(pady="100",padx="90")

mainloop()

