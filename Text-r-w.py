from tkinter import *
from tkinter import filedialog
import PyPDF2
from os import listdir
from os.path import isfile, join







root = Tk()
root.title('Text Editor')
root.iconbitmap("icon.ico")
root.geometry("550x750")

my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

def get_extn(filename):
    return filename[filename.rfind('.') + 1:]

def files_name():
    #mypath = "D:/Studies/Python"
    mypath = filedialog.askdirectory(initialdir="D:/Studies", title="Get Directory")
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for index in range(0, len(onlyfiles) - 1):
        my_text.insert(END, onlyfiles[index] +"\n")




def open_file():
    text_file = filedialog.askopenfilename(initialdir="D:/Studies", title="Open Text File",filetypes=(("All","*.*"),("Text File","*.txt"),("PDF File","*.pdf")))
    extn = get_extn(text_file)
    if extn == "txt":
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        my_text.delete("1.0", END)
        my_text.insert(END, stuff)
        text_file.close()

    elif extn == "pdf":
        if text_file:
            my_text.delete("1.0", END)
            pdf_file = PyPDF2.PdfFileReader(text_file)
            page = pdf_file.getPage(0)
            page_content = page.extract_text()
            my_text.insert(1.0, page_content)
    else:
        pass





def save_txt():
    text_file = filedialog.asksaveasfilename(initialdir="D:/Studies", title="Save Text File",filetypes=(("Text File","*.txt"),("All","*.*"),))
    text_file = open(text_file,'w')
    text_file.write(my_text.get("1.0", END))
    text_file.close()
    my_text.delete(1.0, END)




my_text = Text(my_frame, width=40, height=20, font=("Helvetica", 16))
my_scrollbar.config(command= my_text.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()
my_text.pack(pady=20)

open_btn = Button(root, text="Open File", command=open_file)
open_btn.pack(pady=20)


save_btn = Button(root, text="Save Text File", command=save_txt)
save_btn.pack(pady=20)

files_btn = Button(root, text="files name",command=files_name)
files_btn.pack(pady=20)
root.mainloop()