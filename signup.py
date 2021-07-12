from tkinter import*
import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234@567",database="signup")
# mycursor=mydb.cursor()
# mycursor.execute("create database signup")
# mycursor.execute("create table detail(Uname varchar(20),passwd int(20))")



# mycursor.execute("show tables")
# for tb in mycursor:
#     print(tb)


signup = Tk()
signup.geometry('500x500')
signup.title("Registration Form")
signup.configure(bg='black')

label_0 = Label(signup, text="Registration form",width=20,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_0.place(x=150,y=0)

label_1 = Label(signup, text="FullName",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_1.place(x=0,y=40,)
entry_1 = Entry(signup)
entry_1.place(x=120,y=40)

label_2 = Label(signup, text="Email",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_2.place(x=0,y=80)

entry_2 = Entry(signup)
entry_2.place(x=120,y=80)

label_3 = Label(signup, text="Gender",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_3.place(x=0,y=120)

var = IntVar()
Radiobutton(signup, text="Male",padx = 5, variable=var, value=1).place(x=120,y=120)
Radiobutton(signup, text="Female",padx = 20, variable=var, value=2).place(x=200,y=120)

label_4 = Label(signup, text="Age:",width=7,bg="#11afed",fg="black",font=("TitilliumWeb-Regular", 20))
label_4.place(x=0,y=160)

label_1 = StringVar()
label_2 = StringVar()
label_3 = IntVar()
label_4 = IntVar()



entry_2 = Entry(signup)
entry_2.place()

Button(signup, text='Submit',width=7,height=1,bg='brown',fg='black',font=("TitilliumWeb-Regular", 20)).place(x=0,y=200)


def goback():
    signup.destroy( )
    import main


Button(signup, command=goback, text="Back", width=7, height=1,font=("TitilliumWeb-Regular", 20)).place(x=120,y=200)
signup.mainloop()