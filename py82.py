from tkinter import *
from tkinter import messagebox
# Setting up the main window
root = Tk()
root.title("Denominations Calculator")
root.configure(bg = "light blue")
root.geometry("650x400")

from PIL import Image, ImageTk
#Adding the image and labels in the main window
upload = Image.open("Screenshot 2025-08-26 170042.png")
#Resize the image using resize() method
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image = image, bg = "light blue")
label.place(x = 180, y = 20)

label1 = Label(root, text = "Hey User! Welcome to the Denomination Calculator Application.", bg = "light blue")
label1.place(relx = 0.5, y = 340, anchor = CENTER)

#Function to display a message box and proceed if ok is clicked


def msg():
    MsgBox = messagebox.showinfo("Alert","Do you want to calculate the denomination amount?")
    if MsgBox == "ok" :
        topwin()

#Adding buttons to the main window
button1 = Button(root, text = "Lets, Get Started!!", command = msg, bg = "brown", fg = "white")
button1.place(x = 260, y = 360)

#Function to create a new window
def topwin():
    top = Toplevel()
    top.title("Denominations calculator")
    top.geometry("600x450")
    label = Label(top, text = 'Enter total amount : ', bg = 'light grey')
    entry = Entry(top)
    lbl1 = Label(top, text = "here are the number of notes for each documentation", bg = 'light grey')
    
    l1 = Label(top, text = "2000", bg = 'light grey')
    l2 = Label(top, text = "500", bg = 'light grey')
    l3 = Label(top, text = "100", bg = 'light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())#368700
            note2000 = amount//2000 # 368700//2000=184
            amount =amount% 2000 #700
            note500 = amount // 500 #1
            amount %= 500 #200
            note100 = amount // 100 # 2

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80   )
    btn.place(x=240, y=120   )
    label.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()