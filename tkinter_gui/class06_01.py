from tkinter import *

root = Tk()
root.title('Simple Sum Calculator')

# e = Entry(root, width=50, bg='yellow', fg='white', borderwidth=5)
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    n = e.get()
    n = int(str(n) + str(number))
    e.delete(0,END)
    e.insert(0,n)

def button_clear():
    e.delete(0,END)

def button_add():
    global first_number_to_sum
    first_number_to_sum = e.get()
    e.delete(0,END)

def button_equal():
    # global first_number_to_sum
    second_number_to_sum = e.get()
    e.delete(0,END)
    e.insert(0,int(second_number_to_sum)+int(first_number_to_sum))

padx_value = 40
pady_value = 20
button_1 = Button(root,text='1',padx=padx_value,pady=pady_value,command=lambda: button_click(1))
button_2 = Button(root,text='2',padx=padx_value,pady=pady_value,command=lambda: button_click(2))
button_3 = Button(root,text='3',padx=padx_value,pady=pady_value,command=lambda: button_click(3))
button_4 = Button(root,text='4',padx=padx_value,pady=pady_value,command=lambda: button_click(4))
button_5 = Button(root,text='5',padx=padx_value,pady=pady_value,command=lambda: button_click(5))
button_6 = Button(root,text='6',padx=padx_value,pady=pady_value,command=lambda: button_click(6))
button_7 = Button(root,text='7',padx=padx_value,pady=pady_value,command=lambda: button_click(7))
button_8 = Button(root,text='8',padx=padx_value,pady=pady_value,command=lambda: button_click(8))
button_9 = Button(root,text='9',padx=padx_value,pady=pady_value,command=lambda: button_click(9))
button_0 = Button(root,text='0',padx=padx_value,pady=pady_value,command=lambda: button_click(0))

button_add = Button(root,text='+',padx=padx_value - 1,pady=pady_value,command=button_add)

button_equal = Button(root,text='=',padx=padx_value * 2 + 6,pady=pady_value,command=button_equal)

button_clear = Button(root,text='CLEAR',padx=padx_value * 2 - 8,pady=pady_value,command=button_clear)


#put the button on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_clear.grid(row=5,column=1,columnspan=2)

# def myClick():
#     hello = "Hello " + e.get()
#     # myLabel = Label(root,text="Hello " + e.get())
#     myLabel = Label(root,text=hello)
#     myLabel.pack()


# #creating at button widget
# myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="red")
# myButton = Button(root, text="Click Me!", command=myClick())
# myButton = Button(root, text="Click Me!", padx=50, pady=50)
# myButton = Button(root, text="Click Me!", state=DISABLED )

#shoving it on the screen
# myButton.pack()

root.mainloop()