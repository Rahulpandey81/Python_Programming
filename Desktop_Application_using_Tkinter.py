import tkinter as Rp
from tkinter import messagebox
a=Rp.Tk()

#lbl=Rp.Label(a,text="Welcome User",height=2,width=50,bg="Red",fg="Black").pack()
lblusr=Rp.Label(a,text="UserName",height=1,width=15,bg="pink").grid()
frm=Rp.Frame.config(a,bg="Yellow")
usrname=Rp.Entry(a).grid()
lblfather=Rp.Label(a,text="Father Name",height=1,width=15,bg="pink").grid()
pswd=Rp.Entry(a).grid()
lblmbl=Rp.Label(a,text="Mobile_No",height=1,width=15,bg="pink").grid()
mbl=Rp.Entry(a).grid()
gender=Rp.Label(a,text="Gender",height=1,width=15,bg="pink").grid()
rdoMale=Rp.Radiobutton(a,text="Male",value=0).grid()
rdoFemale=Rp.Radiobutton(a,text="female",value=1).grid()
hobby=Rp.Label(a,text="Hobies",height=1,width=15,bg="pink").grid()
crckt=Rp.Checkbutton(a,text="Cricket").grid()
sngn=Rp.Checkbutton(a,text="Singing").grid()
dncn=Rp.Checkbutton(a,text="dancing").grid()
def Shyam():
    messagebox.showinfo("Message","Data Saved successfully")
btn=Rp.Button(a,text="Save",command=Shyam,bg="Red",height=3,width=10).grid()
def Ram():
    for i in range(1,40):
        ptrn=list(" " * 40)
        ptrn[i]="*" *9
        ptrn[-(i+1)]="*" *9
        print("".join(ptrn))
btn=Rp.Button(a,text="Print X Pattern",bg="Red",command=Ram,height=3,width=20).grid()





