from tkinter import *
from gtts import gTTS
import tkinter
import platform

root = Tk()
root.geometry("450x600")
root.configure(bg='black')
root.title("Make Audio Book")
# Frame ----------------------------------------------------
data = tkinter.Frame(root,bg='white')
data.pack(side=TOP, fill=X)

def login():
    root.destroy()
    import login
def signup():
    root.destroy( )
    import signup

log=Button(data, text = "Login", command = login,width=15,height=3,bg ='#00ebc7', fg='#00214d',)
reg=Button(data, text = "Register", command = signup ,width=15,height=3,bg ='#00ebc7', fg='#00214d')

if platform.system() == "Darwin":
    reg.configure(highlightbackground="#00ebc7", fg="#00214d")
    log.configure(highlightbackground="#00ebc7", fg="#00214d")
else:
    reg.configure(bg="#00ebc7", fg="#00214d")
    log.configure(bg="#00ebc7", fg="#00214d")

log.pack(side=LEFT)
reg.pack(side=RIGHT)

# Frame ----------------------------------------------------
header = tkinter.Frame(root,bg='black')
header.pack(side=TOP, fill=X)
Label(header, text = "To Speak", font=("TitilliumWeb-Regular", 20), bg ='#00ebc7', fg='#00214d').pack()



Msg = StringVar()
Label(root,text ="Enter Text", font=("TitilliumWeb-Regular", 20), bg ='#00ebc7', fg='#00214d').place(x=10,y=100)
entry_field = Entry(root, textvariable = Msg ,width ='40')
entry_field.place(x=10,y=200,)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('tts-save.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Group1 Frame ----------------------------------------------------
body = tkinter.Frame(root)
body.pack(side=BOTTOM, fill=X)

p=Button(body, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width=15,height=3,bg ='#00ebc7', fg='#00214d')
x=Button(body, font = 'arial 15 bold',text = 'EXIT', width=15,height=3, command = Exit,  bg ='#00ebc7', fg='#00214d')
r=Button(body, font = 'arial 15 bold',text = 'RESET',width=15,height=3, command = Reset, bg ='#00ebc7', fg='#00214d')

if platform.system() == "Darwin":  # if its a Mac
    p.configure(highlightbackground="#00ebc7", fg="#00214d")
    x.configure(highlightbackground="#00ebc7", fg="#00214d")
    r.configure(highlightbackground="#00ebc7", fg="#00214d")


else:  # if its Windows or Linux
    p.configure(bg="#00ebc7", fg="#00214d")
    x.configure(bg="#00ebc7", fg="#00214d")
    r.configure(bg="#00ebc7", fg="#00214d")


p.grid(row=0, column=1, padx=5, pady=10)
x.grid(row=0, column=2, padx=5, pady=10)
r.grid(row=0, column=3, padx=5, pady=10)

root.mainloop()
