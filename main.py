import tkinter
from tkinter import *
from tkinter import messagebox
import base64


def decryption():
    if secretkey.get()=="1234":
        root2=Toplevel(root)
        root2.title("Decryption")
        root2.geometry("400x200")
        root2.configure(bg="#00bd56")

        message=inputText.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")
        Label(root2,text="DECRYPT",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(root2,bg="white",relief=GROOVE,wrap=WORD ,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)

        root2.mainloop()

    else :
        messagebox.showerror("encryption","Invalid password")

def encryption():
    if secretkey.get()=="1234":
        root1=Toplevel(root)
        root1.title("Encryption")
        root1.geometry("400x200")
        root1.configure(bg="#ed3833")

        message=inputText.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        Label(root1,text="ENCRYPT",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(root1,bg="white",relief=GROOVE,wrap=WORD ,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)

        root1.mainloop()

    else :
        messagebox.showerror("encryption","Invalid password")




def reset():
    inputText.delete(1.0,END)
    secretkey.delete(0,END)



root=Tk()

root.geometry("480x620")
root.option_add( "*font", "Arial 20  " )
#buttonFont = tkinter.font.Font(family='Helvetica', size=16, weight='bold')
label =Label(root,text="Enter Message" )
label.pack(anchor=tkinter.W,pady=5 ,padx=15)


inputText=Text(root,height=8,width=30)
inputText.pack(padx=15,pady=20)
#global root
#global inputText
label =Label(root,text="Enter your secret key")
label.pack(anchor=tkinter.W,pady=5 ,padx=20)

password=StringVar()
secretkey=Entry(root,textvariable=password,show="*",width=30)
secretkey.pack(padx=15,pady=15)

frame = Frame(root)
frame.pack()
encrypt=Button(frame,text="Encrypt",fg="white",bg="red" ,height=1,width=13 ,command=encryption)
encrypt.pack(side=tkinter.LEFT,pady=2 ,padx=15)

decrypt=Button(frame,text="Decrypt", fg="white",bg="green" ,height=1,width=13,command=decryption)
decrypt.pack(side=tkinter.LEFT,pady=2 ,padx=15)

reset =Button(root,text="Reset", fg="white",bg="blue" ,height=1,width=30 , command=reset)
reset.pack(side=tkinter.BOTTOM,pady=2 ,padx=15)

root.mainloop()
