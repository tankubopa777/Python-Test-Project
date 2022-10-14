from cProfile import label
import imp
from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image

root = Tk()
root.title("QRCode Generator test")
canvas = Canvas(root,width=400,height=500)
canvas.pack()

def generateQRCode():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name+".png"
    print(link_name , " = " ,link)

    url = pyqrcode.create(link)
    url.png(file_name,scale=5)

    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image = image)
    image_label.image=image

#Program name
app_label = Label(root,text="QRCode Generator",font=("Arial",20,"bold"))
canvas.create_window(200,50,window=app_label)
#Name and link
name_label = Label(root,text="QRCode name")
canvas.create_window(200,100,window=name_label)

link_label = Label(root,text="URL ")
canvas.create_window(200,160,window=link_label)

#Textbox
name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry = Entry(root)
canvas.create_window(200,180,window=link_entry)

#Button
button = Button(text="Create QRCode",command=generateQRCode)
canvas.create_window(200,230,window=button)

root.mainloop()