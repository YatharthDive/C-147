from tkinter import*
root=Tk()
root.title("ascii converter")
root.geometry("400x400")
root.configure(background="skyblue")
input_box=Entry(root)
input_box.place(relx=0.5,rely=0.4,anchor=CENTER)

label1 = Label(root, text = "Name in Ascii : ", bg= "light cyan", fg="black")
label2 = Label(root, text = "Encrypted Name : ", bg= "light cyan", fg="black")

def ASCIIconverter():
    input_word=input_box.get()
    for letter in input_word:
        label["text"]+=str(ord(letter))+","
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"]+= str(chr(encrypted))
        
        
btn=Button(root,text="Display the Ascii Code and Encrypted value",command=ASCIIconverter,bg="royalblue",fg="white")
btn.place(relx=0.5,rely=0.6,anchor=CENTER)        
        
btn=Button(root,text="show name in ASCII",bg="red",fg="white",command=ASCIIconverter)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label=Label(root,text="name in ASCII:-",bg="cyan",fg="darkblue")
label.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()

