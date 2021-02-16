import archive

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames

displayText = None


def uploadaction(event=None):
    filename = askopenfilenames()
    if filename:
        print('got file, sending to archive handler')
        print(filename)
        messagebox.showinfo(title="Spore",
                            message="The GUI will not work while uploading, please refer to the CLI for output")
        archive.process(filename)
    else:
        messagebox.showinfo(title="Spore", message="You did not select a File/Folder")


def infobox(msg):
    messagebox.showinfo(title="Spore", message=msg)


def init():
    root = Tk()
    root.geometry("400x245")
    root.title("Spore v0.1")

    thislabel = Label(root, text="Spore super cool file uploading")
    thislabel.pack()
    uploadbutton = Button(root, text="Upload", command=uploadaction)
    uploadbutton.pack()

    global displayText
    displayText = Text(root, height=10, width=50)
    displayText.pack()
    displayText.configure(state='disabled')

    root.mainloop()


def update_links(msg):
    displayText.configure(state='normal')
    displayText.insert(END, msg + '\n')
    displayText.configure(state='disabled')


def clear():
    print('cleared text area')
    displayText.configure(state='normal')
    displayText.delete('1.0', END)
    displayText.configure(state='disabled')
