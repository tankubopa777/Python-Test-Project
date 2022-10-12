from tkinter import *
from googletrans import Translator

def transalate():
    message = text1.get("1.0","end-1c")
    transalator = Translator()
    output = transalator.translate(text=message,src="en",dest="th")
    text2.insert("end",output.text)

def deletemessage():
    text1.delete(1.0,"end")
    text2.delete(1.0,"end")

# Screen
app = Tk()
app.title("Google Transalte with Python")
app.geometry("500x350")
app.maxsize(500,350)
app.maxsize(500,350)

# Widget
label = Label(text="English to Thai",font=("Arial",25,"bold"))
label.place(x=135,y=20)

# Save English
text1 = Text(app,width=30,height=13)
text1.place(x=10,y=70)

# Save Thai
text2 = Text(app,width=30,height=13)
text2.place(x=245,y=70)

# Botton
translateBtn = Button(app,text="แปลภาษา",command=transalate)
translateBtn.place(x=170,y=290)

clearBtn = Button(app,text="ลบข้อความ",command=deletemessage)
clearBtn.place(x=260,y=290)
app.mainloop()
