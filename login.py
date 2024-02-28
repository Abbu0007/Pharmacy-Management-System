from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt
import subprocess


window=Tk()
window.title("LoginIn")
window.geometry("925x500+300+200")
window.configure(bg="lightcyan")
window.resizable(False,False)




img= PhotoImage(file='R.png')
Label(window,image=img,border=0,bg='lightcyan').place(x=0,y=90)


frame=Frame(window,width=350,height=390,bg="lightcyan")
frame.place(x=480,y=50)
heading=Label(frame,text="LogIn",fg="Springgreen",bg="lightcyan",font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
alr=Label(window,text="Not registered yet??",font=('Microsoft Yahei UI Light',10),bg='lightcyan')
alr.place(x=610,y=402)

##--------------------

conn=sqlite3.connect("userdata.db")
cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL)""")

conn.commit()

##---------------

def on_enter(e):
    nam.delete(0,'end')
def on_leave(e):
    if nam.get()=='':
        nam.insert(0,'Username')
nam=Entry(frame,width=25,fg='black',border=0,bg='lightcyan',font=('Microsoft Yahei UI Light',11))
nam.place(x=30,y=100)
nam.insert(0,'Username')
nam.bind("<FocusIn>",on_enter)
nam.bind("<FocusOut>",on_leave)

def on_enter(e):
    usern.delete(0,'end')
def on_leave(e):
    if usern.get()=='':
        usern.insert(0,'Password')
usern=Entry(frame,width=25,fg='black',border=0,bg='lightcyan',font=('Microsoft Yahei UI Light',11))
usern.place(x=30,y=170)
usern.insert(0,'Password')
usern.bind("<FocusIn>",on_enter)
usern.bind("<FocusOut>",on_leave)

def signu():
    window.destroy()
    import signup

def logn():
    username=nam.get()
    password=usern.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result= cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                open_sys_file()
                window.destroy()
                
            else:
                messagebox.showerror('Error', 'Invalid passsword.')
        else:
            messagebox.showerror('Error','Invalid Username')
    else:
        messagebox.showerror('Error','Enter all data')   



def open_sys_file():
    try:
        subprocess.Popen(["python", "ms.py"], shell=True)
    except Exception as e:
        print("Error:", e)
 


##------------------

Button(frame,width=39,pady=7,text="Log In",bg="springgreen",fg='White',border=0,command=logn).place(x=35,y=280)
Button(frame,width=5,pady=5,text="Sign Up",bg="Lightcyan",fg='Black',border=0,command=signu).place(x=270,y=350)

window.mainloop()