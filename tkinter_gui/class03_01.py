from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text='Look I have clicked on the button')
    myLabel.pack()

#creating at button widget
myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
# myButton = Button(root, text="Click Me!", command=myClick())
# myButton = Button(root, text="Click Me!", padx=50, pady=50)
# myButton = Button(root, text="Click Me!", state=DISABLED )

#shoving it on the screen
myButton.pack()

root.mainloop()