from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt

window=Tk()
window.title("Signup")
window.geometry("925x500+300+200")
window.configure(bg="lightcyan")
window.resizable(False,False)

##---------------

conn=sqlite3.connect("userdata.db")
cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL)""")



img= PhotoImage(file='R.png')
Label(window,image=img,border=0,bg='lightcyan').place(x=0,y=90)


frame=Frame(window,width=350,height=390,bg="lightcyan")
frame.place(x=480,y=50)
heading=Label(frame,text="Signup",fg="Springgreen",bg="lightcyan",font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
alr=Label(window,text="Already have an account?",font=('Microsoft Yahei UI Light',10),bg='lightcyan')
alr.place(x=570,y=402)
####-------------------
def on_enter(e):
    nam.delete(0,'end')
def on_leave(e):
    if nam.get()=='':
        nam.insert(0,'Username')
nam=Entry(frame,width=25,fg='black',border=0,bg='lightcyan',font=('Microsoft Yahei UI Light',11))
nam.place(x=30,y=120)
nam.insert(0,'Username')
nam.bind("<FocusIn>",on_enter)
nam.bind("<FocusOut>",on_leave)

def on_enter(e):
    usern.delete(0,'end')
def on_leave(e):
    if usern.get()=='':
        usern.insert(0,'Password')
usern=Entry(frame,width=25,fg='black',border=0,bg='lightcyan',font=('Microsoft Yahei UI Light',11))
usern.place(x=30,y=200)
usern.insert(0,'Password')
usern.bind("<FocusIn>",on_enter)
usern.bind("<FocusOut>",on_leave)

def logn():
    window.destroy()
    import login

def signup():
    username=nam.get()
    password=usern.get()
    if username !='' and password !='':
        cursor.execute('SELECT username FROM users WHERE username=?',[username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error','Username already exists.')
        else:
            encoded_password=password.encode('utf=8')
            hashed_password=bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username,hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created')
    else:
        messagebox.showerror('Error', 'Enter all data.')



##---------------

Button(frame,width=39,pady=7,text="Sign Up",bg="springgreen",fg='White',border=0,command=signup).place(x=35,y=280)
Button(frame,width=5,pady=5,text="Log in",bg="Lightcyan",fg='Black',border=0,command=logn).place(x=270,y=350)
window.mainloop()