# ENHANCEMENT
'''
1. Seperate button for show databases               --- Complete
2. Seperate button for show tables                  --- Complete
3. Clear data                                       --- Incomplete 
4. Clear fields                                     --- Complete
5. Set default                                      --- Complete
6. Change theme - background change with font       --- Complete (partially)

'''

from tkinter import *
import mysql.connector
from tkinter import Tk,Frame,Menu

win = Tk()
win.geometry("650x650")
# win.resizable(0,0)
win.title("Database connection")
logo1 = PhotoImage(file = 'DB.png')
win.iconphoto(False, logo1)

fr1 = Frame(win)
fr1.grid(row=7, columnspan=2)

txtfg = "green"
txtbg = "white"
btnfg = "blue"
btnbg = "lightgrey"
lblfg = "black"


# Logic Functions
# ************************************************************

def showdb():
    uname = txtuser.get()
    pswd = txtpswd.get()
    query = "show databases"
    con = mysql.connector.connect(host="localhost", user=uname, password=pswd)
    cur1 = con.cursor()
    cur1.execute(query)

    i = 0
    
    lbl = Label(win, text="Display Database : ", font=("Arial", 10, "bold"), fg="red")
    lbl.grid(row=6, columnspan=2, pady=5)
    for tbl in cur1 :
        for j in range(len(tbl)):
            t1 = Entry(fr1, width=25, fg="green", font=("Arial", 10, "bold"))
            t1.grid(row = i, column=j, pady=5)
            t1.insert(END,tbl[j])
        i = i+ 1


def clear_data():
    for widgets in fr1.wininfo_children():
        widgets.destroy()


def showtbl():
    dbname = txtdatabase.get()
    uname = txtuser.get()
    pswd = txtpswd.get()
    query = "show tables"
    con = mysql.connector.connect(host="localhost", user=uname, password=pswd, database=dbname)
    cur1 = con.cursor()
    cur1.execute(query)


    i = 0
    lbl = Label(win, text="Display Tables : ", font=("Arial", 10, "bold"), fg="red")
    lbl.grid(row=6, columnspan=2, pady=5)
    for tbl in cur1 :
        for j in range(len(tbl)):
            t1 = Entry(fr1, width=25, fg=txtfg, bg=txtbg, font=("Arial", 10, "bold"))
            t1.grid(row = i, column=j, pady=5)
            t1.insert(END,tbl[j])
        i = i+ 1



def executedb():
    dbname = txtdatabase.get()
    uname = txtuser.get()
    pswd = txtpswd.get()
    query = txtsql.get()
    tbl = txttbl.get()
    con = mysql.connector.connect(host="localhost", user=uname, password=pswd, database=dbname)
    cur1 = con.cursor()
    cur1.execute(query)


    i = 0
    lbl = Label(win, text="Database Display : ", font=("Arial", 10, "bold"), fg="red")
    lbl.grid(row=6, columnspan=2, pady=5)
    for tbl in cur1 :
        for j in range(len(tbl)):
            t1 = Entry(fr1, width=10, fg="green", font=("Arial", 10, "bold"))
            t1.grid(row = i, column=j, pady=5)
            t1.insert(END,tbl[j])
        i = i+ 1

def clrtxt():
    txtdatabase.delete("0","end")
    txtuser.delete("0","end")
    txtpswd.delete("0","end")
    txtsql.delete("0","end")
    txttbl.delete("0","end")

def defautVal():
    txtdatabase.delete("0","end")
    txtuser.delete("0","end")
    txtdatabase.insert(0,"nitesh")
    txtuser.insert(0,"root")

def darkMode():

    win.configure(background="grey25")
    for widgets in fr1.wininfo_children():
        widgets.configure(background ="grey25")



# UserInterface
#************************************************************

menubar = Menu(win)
file = Menu(menubar,tearoff=0)
file.add_command(label="Show Database", command=executedb)
file.add_command(label="Create Database")
sub = Menu(file, tearoff = 0)
sub.add_command(label = "mysql")
sub.add_command(label = "oracle", underline=0)
sub.add_command(label = "sqlserver")
sub.add_command(label = "mongodb")
file.add_cascade(label = "Open Database", menu = sub)
file.add_command(label="Remove Database")
file.add_separator()
file.add_command(label="Create Table")
file.add_separator()
file.add_command(label="Quit", command = exit)
menubar.add_cascade(label="Database", menu=file)

record = Menu(menubar,tearoff=0)
record.add_command(label="Insert")
record.add_command(label="Delete")
record.add_command(label="Update")
record.add_separator()
record.add_command(label="Custom Query")
menubar.add_cascade(label="Record", menu=record)

win.config(menu=menubar)


l1 = Label(win, text="Database Name : ", fg=lblfg, font=("Arial", 10, "bold"))
l1.grid(row = 0 , column=0, pady= 10, sticky=E)

txtdatabase = Entry(win, fg=txtfg, bg=txtbg, width=35, font=("Arial", 10, "bold"))
txtdatabase.grid(row=0, column=1, pady=10)


l2 = Label(win, text="Username : ", fg=lblfg, font=("Arial", 10, "bold"))
l2.grid(row=1, column=0, pady=10, sticky=E)

txtuser = Entry(win, fg=txtfg, bg=txtbg, width=35, font=("Arial", 10, "bold"))
txtuser.grid(row=1, column=1, pady=10)


l3 = Label(win, text="Password : ", fg=lblfg, font=("Arial", 10, "bold"))
l3.grid(row = 2 , column=0, pady= 10, sticky=E)

txtpswd = Entry(win, fg=txtfg, bg=txtbg, width=35, font=("Arial", 10, "bold"))
txtpswd.grid(row=2, column=1, pady=10)

l4 = Label(win, text="SQL Statement : ", fg=lblfg, font=("Arial", 10, "bold"))
l4.grid(row=3, column=0, pady=10, sticky=E)

txtsql = Entry(win, fg=txtfg, bg=txtbg, width=35, font=("Arial", 10, "bold"))
txtsql.grid(row=3, column=1, pady=10)

l5 = Label(win, text="Table Name : ", fg=lblfg, font=("Arial", 10, "bold"))
l5.grid(row=4, column=0, pady=10, sticky=E)

txttbl = Entry(win, fg=txtfg, bg=txtbg, width=35, font=("Arial", 10, "bold"))
txttbl.grid(row=4, column=1, pady=10)


b1 = Button(win, text="Execute", fg=btnfg, bg=btnbg, width=13, font=("Arial", 10, "bold"), command=executedb)
b1.grid(row=0, column=2, padx=5, sticky=W)

b2 = Button(win, text="Clear Inputs", fg=btnfg, bg=btnbg, width=13, font=("Arial", 10, "bold"), command = clrtxt)
b2.grid(row=1, column=2, padx=5, sticky=E)

b3 = Button(win, text="Show Databases", fg=btnfg, bg=btnbg, width=13, font=("Arial", 10,"bold"), command=showdb)
b3.grid(row=2, column=2, padx=5, sticky=E)

b4 = Button(win, text="Show Tables", fg=btnfg, bg=btnbg, width=13, font=("Arial", 10,"bold"), command=showtbl)
b4.grid(row=3, column=2, padx=5, sticky=E)

b5 = Button(win, text="Default Entries", fg=btnfg, bg=btnbg, width=13, font=("Arial",10, "bold"), command=defautVal)
b5.grid(row=4, column=2, padx=5, sticky=E)

b6 = Button(win, text="Dark Mode Theme", fg=btnfg, bg=btnbg, width=15, font=("Arial",10,"bold"), command=darkMode)
b6.grid(row=0, column=3, padx=4, sticky=E)

b7 = Button(win, text="Clear Data", fg=btnfg, bg=btnbg, width=15, font=("Arial",10,"bold"), command=clear_data)
b7.grid(row=1, column=3, padx=4, sticky=E)

win.mainloop()