import serial
import tkinter as tk
root=tk.Tk()
root.title("IOT Remote")
frm=tk.Frame.config(root,bg='yellow')
root.geometry('200x250')
root.resizable(0,0)
ard=serial.Serial('/dev/ttyACM0','9600')
def ledRed():
    ard.write(str.encode('3'))
btn=tk.Button(root,text="Red",command=ledRed,fg='Green',bg='Red',height=2,width=10,border=5)
btn.place(x=40,y=20)
def ledGreen():
    ard.write(str.encode('1'))
btnGreen=tk.Button(root,text="Green",command=ledGreen,fg='red',bg='Green',height=2,width=10,border=5)
btnGreen.place(x=40,y=60)
def ledBlue():
    ard.write(str.encode('2'))
btnBlue=tk.Button(root,text="Blue",command=ledBlue,fg='black',bg='blue',height=2,width=10,border=5)
btnBlue.place(x=40,y=100)
def ledOff():
    ard.write(str.encode('0'))
btnOff=tk.Button(root,text='OFF',command=ledOff,bg='black',fg='white',height=2,width=10,border=5)
btnOff.place(x=40,y=140)
def relayTest():
    ard.write(str.encode('5'))
btnRelay=tk.Button(root,text='GOTO AC POWER',command=relayTest,fg="black",bg="darkred",height=3,width=10,border=5)
btnRelay.place(x=40,y=180)
root.mainloop()

