from tkinter import *
import random
root=Tk()
root.title("Color Generator")
root.geometry("300x400")


dictionary={'Colors':["black","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def change():
    number=random.randint(0,8)
    root.configure(background=dictionary["Colors"][number])
    

button=Button(root,text="Click Me", command=change)
button.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()