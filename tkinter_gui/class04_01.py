from tkinter import *

root = Tk()

# e = Entry(root, width=50, bg='yellow', fg='white', borderwidth=5)
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0,"Enter your name here")

def myClick():
    hello = "Hello " + e.get()
    # myLabel = Label(root,text="Hello " + e.get())
    myLabel = Label(root,text=hello)
    myLabel.pack()

#creating at button widget
myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="red")
# myButton = Button(root, text="Click Me!", command=myClick())
# myButton = Button(root, text="Click Me!", padx=50, pady=50)
# myButton = Button(root, text="Click Me!", state=DISABLED )

#shoving it on the screen
myButton.pack()

root.mainloop()