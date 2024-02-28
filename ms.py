import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tablle



app= customtkinter.CTk()
app.title('Pharmacy Management System')
app.geometry('1000x600')
app.config(bg='Black')
app.resizable(False,False)
def create_title_with_border(root, title_text):
    title_frame = tk.Frame(root, bd=2, relief="groove")
    title_frame.pack(side="top", fill="x")
    title_label = tk.Label(title_frame, text=title_text, font=("Palatino Linotype", 25,'bold'), bg="White")
    title_label.pack(padx=10, pady=25)


create_title_with_border(app, "Pharmacy Management System")

font1= ('Microsoft Yahei UI Light',20,'bold')
font2= ('Microsoft Yahei UI Light',12,'bold')
font3= ('Microsoft Yahei UI Light',27,'bold','underline')

def on_entry_click(event):
    if issue_entry.get() == 'YYYY-MM-DD':
        issue_entry.delete(0, "end") 
        issue_entry.insert(0, '') 
def on_eentry_click(event):
    if exp_entry.get() == 'YYYY-MM-DD':
        exp_entry.delete(0, "end") 
        exp_entry.insert(0, '') 
    

def on_focusout(event):
    if issue_entry.get() == '':
        issue_entry.insert(0, 'YYYY-MM-DD')
def on_ffocusout(event):
    if exp_entry.get() == '':
        exp_entry.insert(0, 'YYYY-MM-DD')   
      

def add_to_treeview():
    Pharmacy = tablle.fetch_Pharmacy()
    for item in tree.get_children():
        tree.delete(item)
    for Pharmac in Pharmacy:
        tree.insert('',END, values=Pharmac)

def insert():
    RefNo=ref_entry.get()
    Name=nam_entry.get()
    Company=com_entry.get()
    Issue=issue_entry.get()
    Expiry=exp_entry.get()
    Classi=variable1.get()
    if not(RefNo and Name and Company and Issue and Expiry and Classi):
        messagebox.showerror('Error','Enter all fields')
    elif tablle.Ref_no_exists(RefNo):
        messagebox.showerror('Error','ID already exists')
    else:
        tablle.insert_medicine(RefNo,Name,Company,Issue,Expiry,Classi)
        add_to_treeview()
        messagebox.showinfo('Success','Data has been inserted')

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    ref_entry.delete(0,END)
    nam_entry.delete(0,END)
    com_entry.delete(0,END)
    issue_entry.delete(0,END)
    exp_entry.delete(0,END)
    variable1.set('General Sales List')

def display_data(event):
    selected_item=tree.focus()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        ref_entry.insert(0,row[0])
        nam_entry.insert(0,row[1])
        com_entry.insert(0,row[2])
        issue_entry.insert(0,row[3])
        exp_entry.insert(0,row[4])
        variable1.set(row[5])
    else:
        pass

def update():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a medicine to update')
    else:
        RefNo=ref_entry.get()
        Name=nam_entry.get()
        Company=com_entry.get()
        Issue=issue_entry.get()
        Expiry=exp_entry.get()
        Classi=variable1.get()
        tablle.update_medicine(Name,Company,Issue,Expiry,Classi,RefNo)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been updated')


def delete():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a Medicine to delete')
    else:
        Ref_no=ref_entry.get()
        tablle.delete_medicine(Ref_no)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted')





ref_label=customtkinter.CTkLabel(app,font=font1,text="Ref.No:",text_color='White',bg_color='Black')
ref_label.place(x=20,y=150)

ref_entry=customtkinter.CTkEntry(app,font=font2,text_color='Black',fg_color='White',border_color='Dark Blue',border_width=2,width=180)
ref_entry.place(x=140,y=150)

nam_label=customtkinter.CTkLabel(app,font=font1,text="Name:",text_color='White',bg_color='Black')
nam_label.place(x=20,y=210)

nam_entry=customtkinter.CTkEntry(app,font=font2,text_color='Black',fg_color='White',border_color='Dark Blue',border_width=2,width=180)
nam_entry.place(x=140,y=210)

com_label=customtkinter.CTkLabel(app,font=font1,text="Company:",text_color='White',bg_color='Black')
com_label.place(x=20,y=270)

com_entry=customtkinter.CTkEntry(app,font=font2,text_color='Black',fg_color='White',border_color='Dark Blue',border_width=2,width=180)
com_entry.place(x=140,y=270)

issue_label=customtkinter.CTkLabel(app,font=font1,text="IssuedOn:",text_color='White',bg_color='Black')
issue_label.place(x=20,y=330)

issue_entry=customtkinter.CTkEntry(app,font=font2,text_color='Black',fg_color='White',border_color='Dark Blue',border_width=2,width=180)
issue_entry.place(x=140,y=330)
issue_entry.insert(0, 'YYYY-MM-DD')
issue_entry.bind('<FocusIn>', on_entry_click)
issue_entry.bind('<FocusOut>', on_focusout)

exp_label=customtkinter.CTkLabel(app,font=font1,text="ExpiryDate:",text_color='White',bg_color='Black')
exp_label.place(x=20,y=390)


exp_entry=customtkinter.CTkEntry(app,font=font2,text_color='Black',fg_color='White',border_color='Dark Blue',border_width=2,width=180)
exp_entry.place(x=140,y=390)
exp_entry.insert(0, 'YYYY-MM-DD')
exp_entry.bind('<FocusIn>', on_eentry_click)
exp_entry.bind('<FocusOut>', on_ffocusout)

class_label=customtkinter.CTkLabel(app,font=font1,text="Class:",text_color='White',bg_color='Black')
class_label.place(x=20,y=450)

options=['General Sales List','Pharmacy Medicine','Prescription Only Medicine','Controlled Drugs']
variable1= StringVar()

class_options=customtkinter.CTkComboBox(app,font=font2,text_color='Black', fg_color='White', dropdown_hover_color='Dark blue', button_hover_color='dark blue', border_color='dark blue',width=180,variable=variable1,values=options, state='readonly')
class_options.set('General Sales List')
class_options.place(x=140,y=450)



add_button= customtkinter.CTkButton(app,command=insert,font=font1,text_color='Black',text='Add Medicine',fg_color='white',hover_color='green',bg_color='black',corner_radius=15,width=260)
add_button.place(x=20,y=500)

new_button= customtkinter.CTkButton(app,command=lambda:clear(True),font=font1,text_color='Black',text='New Medicine',fg_color='white',hover_color='yellow',bg_color='black', corner_radius=15, width=260)
new_button.place(x=20,y=560)

update_button= customtkinter.CTkButton(app,command=update,font=font1,text_color='Black',text='Update Medicine',fg_color='white',hover_color='yellow',bg_color='black', corner_radius=15, width=260)
update_button.place(x=370,y=560)

delete_button= customtkinter.CTkButton(app,command=delete,font=font1,text_color='Black',text='Delete Medicine',fg_color='white',hover_color='red',bg_color='black', corner_radius=15, width=260)
delete_button.place(x=720,y=560)

style=ttk.Style(app)
ttk.Style().theme_use('clam')
style.configure('Treeview',font=font2,foreground='white',background='black',fieldbackground='#313837')
style.map('Treeview',background=[('selected','#1A8F2D')])

tree=ttk.Treeview(app,height=18)

tree['columns']=('Ref No.','Name','Company','Issue Date','Expiry Date','Classi')

tree.column('#0',width=0, stretch=tk.NO)
tree.column('Ref No.', anchor=tk.CENTER,width=110)
tree.column('Name', anchor=tk.CENTER,width=110)
tree.column('Company', anchor=tk.CENTER,width=110)
tree.column('Issue Date', anchor=tk.CENTER,width=110)
tree.column('Expiry Date', anchor=tk.CENTER,width=110)
tree.column('Classi', anchor=tk.CENTER,width=110)


tree.heading('Ref No.',text='Ref No.')
tree.heading('Name',text='Name')
tree.heading('Company',text='Company')
tree.heading('Issue Date',text='Issue Date')
tree.heading('Expiry Date',text='Expiry Date')
tree.heading('Classi',text='Class')


tree.place(x=330,y=120)
tree.bind('<ButtonRelease>', display_data)

add_to_treeview()

app.mainloop()