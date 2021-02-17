import archive

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames

VERSION = "2.1"
GITHUB = "https://github.com/Apathetic-Development-Team/spore"

displayText = None

def uploadaction(event=None):
    filename = askopenfilenames()
    if filename:
        print('got file, sending to archive handler')
        print(filename)
        archive.process(filename)
    else:
        messagebox.showinfo(title="Spore - error", message="You did not select a File/Folder")


def infobox(msg):
    messagebox.showinfo(title="Spore - message", message=msg)


def init():
    root = Tk()
    root.geometry("400x245")
    root.title(f"🦠 Spore v{VERSION} 🦠")

    # the icon
    photo = PhotoImage(file="images/icon.png")
    root.iconphoto(False, photo)

    # the label at the top
    header = Label(root, text="Spore - file uploading made easy", bg="black", fg="white", font=('Verdana', 20),)
    header.pack(fill=X, pady=(0,15))
    
    # the button to browse a file and upload it
    uploadbutton = Button(root, text="Upload file",font=('Verdana', 15), command=uploadaction, relief='flat')
    uploadbutton.pack()

    # the URLs that will be displayed
    global displayText
    displayText = Text(root, height=10, width=50)
    displayText.configure(state='disabled')
    displayText.pack()

    # the label at the bottom
    footer = Button(root, command=opengithub, text=f"Github: {GITHUB.replace('https://', '')}", bg="black", fg="black", font=('Verdana', 10))
    footer.pack(fill=X, side=BOTTOM)

    root.mainloop()

def opengithub():
    from webbrowser import open
    open(GITHUB, new=2)

def update_links(msg):
    displayText.configure(state='normal')
    displayText.insert(END, msg + '\n')
    displayText.configure(state='disabled')


def clear():
    print('cleared text area')
    displayText.configure(state='normal')
    displayText.delete('1.0', END)
    displayText.configure(state='disabled')
