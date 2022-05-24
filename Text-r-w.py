from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Text Editor')
root.iconbitmap("icon.ico")
root.geometry("500x700")


def open_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open Text File",filetypes=(("Text File","*.txt"),("All","*.*"),))
    text_file = open(text_file,'r')
    stuff = text_file.read()
    my_text.delete("1.0",END)
    my_text.insert(END, stuff)
    text_file.close()


def save_txt():
    text_file = filedialog.asksaveasfilename(initialdir="C:/", title="Save Text File",filetypes=(("Text File","*.txt"),("All","*.*"),))
    text_file = open(text_file,'w')
    text_file.write(my_text.get("1.0", END))
    text_file.close()
    my_text.delete(1.0, END)




my_text = Text(root, width=40, height=20, font=("Helvetica", 16))

my_text.pack(pady=20)

open_btn = Button(root, text="Open Text File", command=open_txt)
open_btn.pack(pady=20)

save_btn = Button(root, text="Save Text File", command=save_txt)
save_btn.pack(pady=20)


root.mainloop()