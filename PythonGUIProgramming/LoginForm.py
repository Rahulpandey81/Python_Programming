import tkinter as tk
from tkinter import messagebox
btn=tk.Tk()
frm=tk.Frame.config(btn,bg="Yellow")
lblHeading=tk.Label(btn,text="User Login Interface",fg="Red",bg="Black",height=2,width=20).grid()
lblUser=tk.Label(btn,text="User Name",bg="Red",width=17).grid()
entry=tk.Entry(btn)
entry.grid()
lblPassword=tk.Label(btn,text="Password",bg="Red",width=17).grid()
entry1=tk.Entry(btn,show="*")
entry1.grid()
def lgn():
    
    a=entry.get()
    b=entry1.get()
    if(a=="Ram" and b=="kumar"):
        messagebox.showinfo("Message","Successfull Login")
    else:
        messagebox.showinfo("Message","Invalid Credentials")
    
    
btnSave=tk.Button(btn,text="Login",bg="Red",command=lgn).grid()
