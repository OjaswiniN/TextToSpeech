from tkinter import *
import tkinter
import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234@567", database="signup")
# mycursor = mydb.cursor( )
# mycursor.execute("create database signup")
# mycursor.execute("create table detail(Uname varchar(20),passwd int(20))")



# mycursor.execute("show tables")
# for tb in mycursor:
#     print(tb)

def LoginPage():
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("500x500")
    login_screen.configure(bg='black')

    Label(login_screen, text="Please enter Login details",bg="#11afed",fg="black").place(x=150,y=0)

    Label(login_screen, text="Username").place(x=10,y=40,)

    username_entry = Entry(login_screen, textvariable="username")
    username_entry.place(x=120,y=40,)

    Label(login_screen, text="Password").place(x=10,y=80,)

    password_entry = Entry(login_screen, textvariable="password", show= '*')
    password_entry.place(x=120,y=80,)

    def login():
        if username_entry.get()=='admin' and password_entry.get() =='123':
            print("Login Sucessful")
            login_screen.destroy( )
            import main
        else:
            message = tkinter.Frame(login_screen, bg='white')
            message.pack(side=TOP, fill=X)
            Label(message,text="Unknown User").pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login",command=login,width=10, height=1).place(x=10,y=120,)

    def back():
        login_screen.destroy( )
        import main
    Button(login_screen, command=back,text="Back", width=10, height=1).place(x=120,y=120,)
    login_screen.mainloop()



LoginPage()