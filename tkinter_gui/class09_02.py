from tkinter import *
from PIL import ImageTk,Image

next_image = 0


root = Tk()
root.title('Learn to insert Icons, Images and Exit Button')
root.iconbitmap(r'C:\myScripts\GitHub\python\tkinter_gui\images\paperPlane.ico')

my_img0 = ImageTk.PhotoImage(Image.open(r'C:\myScripts\GitHub\python\tkinter_gui\images\paperPlane.png'))
my_img1 = ImageTk.PhotoImage(Image.open(r'C:\myScripts\GitHub\python\tkinter_gui\images\aviao1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open(r'C:\myScripts\GitHub\python\tkinter_gui\images\aviao2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open(r'C:\myScripts\GitHub\python\tkinter_gui\images\aviao3.jpg'))

image_list = [my_img0,my_img1,my_img2,my_img3]

status = Label(root, text="Image 1 of 5")

def foward():
    global next_image, my_label, button_foward

    next_image += 1
    print(next_image)
    if next_image > len(image_list)-1:
        next_image = 0
        print(next_image)
    elif next_image == 0:
        button_foward = Button(root,text='>>',state=DISABLED)

    my_label.grid_forget()
    my_label = Label(image=image_list[next_image])
    my_label.grid(row=0,column=0,columnspan=3)

def back():
    global next_image, my_label

    next_image -= 1
    if next_image < -len(image_list)+1:
        next_image = 0

    my_label.grid_forget()
    my_label = Label(image=image_list[next_image])
    my_label.grid(row=0,column=0,columnspan=3)

    # if next_image == 0:
    #     button_back = Button(root,text='<<',state=DISABLED)

my_label = Label(image=image_list[0])
my_label.grid(row=0,column=0,columnspan=3)

button_back = Button(root,text='<<',command=lambda:back())
button_exit = Button(root,text='EXIT',command=root.quit)
button_foward = Button(root,text='>>',command=lambda:foward())

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_foward.grid(row=1,column=2)

# button_quit = Button(root,text="quit application",command=root.quit)
# button_quit = Button(root,image=my_img,command=root.quit)
# button_quit.pack()


root.mainloop()