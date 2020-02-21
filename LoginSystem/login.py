import tkinter as tk
from tkinter import *
from tkinter import messagebox

from tkintertable.Tables import TableCanvas
import csv
import getpass
from tkintertable.TableModels import TableModel
def datafrommssql():
    global sql
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=.\SQLEXPRESS;'
                          'Database=Toucan;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Masini')
    row = cursor.fetchall()
    with open('test.csv', 'w', newline='') as f:
        a = csv.writer(f, delimiter=',')
        a.writerow(["Id", "Marca", "Capacitate", "Km", "Pret","Combustibil","An","Descriere","CodSasiu"])  ## etc
        a.writerows(row)
def exista():
    ok=IntVar()
    nr=0
    rez = data.split('\n')
    for x in rez:
        if nr>=1:
         if x is not None:
                rez = data.split(',')
                if username.get() == rez[0]:
                  if password.get() == rez[0]:
                       ok=1
                  else:
                       eok=0
                else:
                    ok=0
         else:
            ok=0
         nr+=1
def verify():
    ok=IntVar()
    rez=data.split('\n')
    nr=0
    for x in rez:
     if nr >= 1:
        rez1=x.split(',')
        if username.get() == rez1[0]:
            if password.get() == rez1[1]:
              ok=1
              break
            else:
               ok=0
        else:
           ok=0
     nr+=1
    if ok == 1:
        return 1
    return 0
def buy():
    global id1
    global sql
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=.\SQLEXPRESS;'
                          'Database=Toucan;'
                          'Trusted_Connection=yes;')
    query='DELETE FROM dbo.Masini WHERE Id='+str(id1.get())
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()

def register():
    global data
    o = open('logindata.txt', 'a+')
    if username.get() != "" and password.get() != "":
        if exista() is None or exista() == 0:
            o.write(username.get() + ',' + password.get() + "\n")
            o.flush()
        o.close()
        f = open('logindata.txt', 'r+')
        data = f.read()
        print(data)
        f.close()
    else:
        messagebox.showinfo("Inregistrare","Introduceti un nume si o parola.")

def login():

    if username.get()!="" and password.get()!="":
      if verify()==1:
          _frame2()
    else:
        messagebox.showinfo("Login","Introduceti nume/parola")
def _frame2():
    frame.destroy()
    frame2 = tk.Tk()
    frame2.title('Frame2')
    frame2.geometry('1000x300')
    tframe = Frame(frame2)
    tframe.pack()
    datafrommssql()
    table = TableCanvas(tframe, editable=False,read_only=True,rows=5, cols=5, height=110,width=939)
    table.importCSV('test.csv')
    Entry(frame2, text='', textvariable=id1).pack()
    Button(frame2, text="Buy car", command=buy).pack()
    table.show()

def mainscreen():
    global data
    f = open('logindata.txt', 'r+')
    data = f.read()
    f.close()
    global frame
    global canvas
    frame = tk.Tk()
    frame.title('Project')
    frame.geometry('300x140')
    global username
    global password
    username = StringVar()
    password = StringVar()
    Label(frame, text='Username ').pack()
    Entry(frame, text='', textvariable=username).pack()
    Label(frame, text='Password ').pack()
    Entry(frame, text='', textvariable=password,show="*").pack()
    Button(frame, text="Login", command=login).pack()
    Button(frame, text="Register", command=register).pack()
    tk.mainloop()
mainscreen()