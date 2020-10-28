from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to insert Icons, Images and Exit Button')
root.iconbitmap(r'C:\myScripts\GitHub\python\tkinter_gui\paperPlane.ico')

my_img = ImageTk.PhotoImage(Image.open(r'C:\myScripts\GitHub\python\tkinter_gui\paperPlane.png'))
my_label = Label(image=my_img)
my_label.pack()



button_quit = Button(root,text="quit application",command=root.quit)
# button_quit = Button(root,image=my_img,command=root.quit)
button_quit.pack()


root.mainloop()