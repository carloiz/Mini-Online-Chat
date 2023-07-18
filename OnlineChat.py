import time
import tkinter as tk
import mysql.connector 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb

server = "sql6.freemysqlhosting.net"
user = "sql6633475"
pasx = "5kSRsCYA35"
db = "sql6633475"

try:
    conn = mysql.connector.connect(host=server,username=user,password=pasx,database=db)
    connect = conn.cursor()
except ValueError as e:
    mb.showinfo("Note", "INTERNET CONNECTION NOT DETECTED")



root = tk.Tk()
root.title("STRANGERS MESSAGES")
root.geometry("1500x400")
root.config(bg="lightblue")
root.resizable(False,False)

tree=ttk.Treeview(root)

tree['show']='headings'

s=ttk.Style(root)
s.theme_use("clam")

s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground='red', font=('Helvetica', 11, "bold"))

tree["columns"]=("ID","Username","Message")

tree.column("ID", width=50, minwidth=50, anchor=tk.CENTER)
tree.column("Username", width=150, minwidth=150, anchor=tk.CENTER)
tree.column("Message", width=1200, minwidth=1200, anchor=tk.CENTER)

tree.heading("ID", text="ID", anchor=tk.CENTER)
tree.heading("Username", text="USER", anchor=tk.CENTER)
tree.heading("Message", text="MESSAGE", anchor=tk.CENTER)

def meeeeeeeeennnNNN(tree):
    items=tree.get_children()
    for item in items:
        tree.delete(item)
    i = 0
    connect.execute("select * from strangers order by ID desc")
    for ro in connect:
        tree.insert('', i, text="", values=(ro[0],ro[1],ro[2]))
        i = i + 1
    time.sleep(2)
    meeeeeeeeennnNNN(tree)
meeeeeeeeennnNNN(tree)

vsb = ttk.Scrollbar(root, orient="vertical")
vsb.configure(command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side= RIGHT)

tree.pack()

search_i=tk.StringVar()
search_q=tk.StringVar()

l1=Label(root,text="USERNAME:", width=10, font=('Times', 11, 'bold'))
e1=Entry(root, textvariable=search_q, width=30, font=('calibri', 13, 'bold')) 
l1.place(x=190, y=260)
e1.place(x=300, y=260) 
l2=Label(root,text="TYPE A MESSAGE HERE:", width=20, font=('Times', 11, 'bold'))
e2=Entry(root, textvariable=search_i, width=100, font=('calibri', 13, 'bold')) 
l2.place(x=100, y=300)
e2.place(x=300, y=300) 

def operation():
    search_v=search_i.get()
    search_x=search_q.get()

    if search_v == "" or search_x == "":
        mb.showinfo("Note", "Fill Up Fields")
    else:
        connect.execute("insert into strangers (user, message) values ('"+ search_x +"','"+ search_v +"')")
        conn.commit()
        e1.delete(0,END)
        e2.delete(0,END)
        meeeeeeeeennnNNN(tree)


button = tk.Button(root, text="Send a Message", command=lambda: operation())
button.configure(font=('calibri', 14, 'bold'), bg= 'blue', fg= 'white')
button.place(x=300, y=330)

root.mainloop()
