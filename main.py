from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("400x400")
screen.title("E&D")
screen.configure(bg="Black")
def encrypt():
    password = code.get()
    if password == "111":
        screen1= Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("300x300")
        screen1.configure(bg="green")

        message = textA.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text = "Encrypted Code", font = "impact 14 bold").place(x=5, y=5)
        text2 = Text(screen1, font = "30", bd = "4", wrap = WORD)
        text2.place(x=5, y=40, width = 290, height = 150)
        text2.insert(END, encrypt)

    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key")
    elif(password!="111"):
        messagebox.showerror("Oops","incorrect password")
def decrypt():
    password = code.get()
    if password == "111":
        screen2= Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("300x300")
        screen2.configure(bg="green")

        message = textA.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2, text = "Decrypted Code", font = "impact 14 bold").place(x=5, y=5)
        text2 = Text(screen2, font = "30", bd = "4", wrap = WORD)
        text2.place(x=5, y=40, width = 290, height = 150)
        text2.insert(END, encrypt)

    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key")
    elif(password!="111"):
        messagebox.showerror("Oops","incorrect password")
def reset():
    textA.delete(1.0, END)
    code.set("")

#label
Label(screen,text = "Enter the text for E&D", font="impack 10 bold", bg="Green").place(x=125,y=10)
#text
textA = Text(screen, bd= 4, font="20")
textA.place(x=10, y=45, width = 380, height =30)
#label
Label(screen,text = "Enter Secret Key", font = "arial 10 ").place(x=150, y=100)
#entry
code = StringVar()
Entry(textvariable = code, bd=4, font = "20",show="😁").place(x=90, y=140)
#button
Button(screen, text = "ENCRYPT", font = "arial 12 bold", bg="red",fg="black", command=encrypt).place(x=60,y=190)
Button(screen, text = "DECRYPT", font = "arial 12 bold", bg="green",fg="black", command=decrypt).place(x=250,y=190)
Button(screen, text = "RESET", font = "arial 12 bold ", bg="yellow",fg="black", command=reset).place(x=165,y=250)
mainloop()