# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:05:50 2020

@author: ASUS
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

mainwindow=tk.Tk()
mainwindow.title('Managment')
mainwindow.resizable(width=False,height=False)
mainwindow.geometry('{}x{}'.format(1350,900))
TABLE_NAME = "management_table"
TEACHER_ID = "teacher_id"
TEACHER_NAME = "teacher_name"
TEACHER_COLLEGE = "teacher_college"
TEACHER_ADDRESS = "teacher_address"
TEACHER_PHONE = "teacher_phone"

connection=sqlite3.connect('management.db')
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + TEACHER_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   TEACHER_NAME + " TEXT, " + TEACHER_COLLEGE + " TEXT, " +
                   TEACHER_ADDRESS + " TEXT, " + TEACHER_PHONE + " INTEGER);")
qlabel=tk.Label(mainwindow,text='TEACHER MANAGMENT SYSTEM SMK MARDI YUANA CIANJUR',width=58,bg='LIGHT BLUE')
qlabel.config(font=("Sylfaen", 30))
qlabel.grid(row=0, columnspan=2, padx=(5,5), pady=(30, 0))

idlabel = tk.Label(mainwindow, text="ID", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),pady=(30, 0))
nameLabel = tk.Label(mainwindow, text="NAME", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0),pady=(30, 0))
collageLabel = tk.Label(mainwindow, text="COLLEGE", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
phoneLabel = tk.Label(mainwindow, text="PHONE", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))
addressLabel = tk.Label(mainwindow, text="ADDRESS", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))

idEntry = tk.Entry(mainwindow, width = 30)
nameEntry = tk.Entry(mainwindow, width = 30)
collegeEntry = tk.Entry(mainwindow, width = 30)
phoneEntry = tk.Entry(mainwindow, width = 30)
addressEntry = tk.Entry(mainwindow, width = 30)

idEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
nameEntry.grid(row=2, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=5, column=1, padx=(0,10), pady = 20)
Button(mainwindow,text="Insert", command=lambda :takeNameInput()).grid(row=6,column=0,pady=10)
Button(mainwindow,text="UPDATE", command=lambda :UPDATE()).grid(row=6,column=1)
Button(mainwindow,text="DELETE", command=lambda :DELETE()).grid(row=7,column=0,pady=10)
Button(mainwindow,text="SHOW", command=lambda :SHOW()).grid(row=7,column=1)
def takeNameInput():
    global idEntry,nameEntry, collegeEntry, phoneEntry, addressEntry
    # global username, collegeName, phone, address
    global list
    global TABLE_NAME,TEACHER_ID,TEACHER_COLLEGE,TEACHER_NAME,TEACHER_ADDRESS,TEACHER_PHONE
    iidname = int(idEntry.get())
    idEntry.delete(0, tk.END)
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)  #To clear fields after insertion
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    
    connection.execute("insert into"+ TABLE_NAME + " ( " + TEACHER_ID + ", " + TEACHER_NAME + ", " +
                       TEACHER_COLLEGE + ", " + TEACHER_ADDRESS + ", " +
                       TEACHER_PHONE + " ) VALUES (" + str(iidname) + ", '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")
    
def DELETE():
    global id,miniwindow
    miniwindow=tk.Tk()
    miniwindow.title('DELETE DATA')
    miniwindow.geometry('{}x{}'.format(400, 300))
    hea=tk.Label(miniwindow,text='Enter the ID of TEACHER').grid(row=0,column=0,padx=50,pady=80)
    id=tk.Entry(miniwindow)
    id.grid(row=0,column=1)
    but=tk.Button(miniwindow,text='Delete',command=lambda:sdelete())
    but.grid(row=1,column=1)
    miniwindow.mainloop()

def sdelete():
    id1=int(id.get())
    query=connection.execute("SELECT * FROM "+TABLE_NAME +" WHERE "+TEACHER_ID +" = {}".format(id1))
    # query=connection.fetchone()[0]
    if query:
        connection.execute("DELETE FROM " +TABLE_NAME + " WHERE " +TEACHER_ID +" =  {}".format(id1) )
        connection.commit()
        miniwindow.destroy()
        messagebox.showinfo('DONE',"Data has been deleted")
    else:
        messagebox.showerror("ERROR","Sorry ,No teacher with this id exist.")

def UPDATE():
    iidname = int(idEntry.get())
    idEntry.delete(0, tk.END)
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)  # To clear fields after insertion
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("UPDATE "+TABLE_NAME+" SET "+ TEACHER_NAME+" = " +"'"+username+"' ,"+TEACHER_COLLEGE+" ="+"'"+collegeName+"' ,"
                       +TEACHER_PHONE+" ="+  str(phone) + " ,"+TEACHER_ADDRESS+" ="+"'"+address+"' WHERE "+TEACHER_ID+" = {}".format(iidname))
    connection.commit()
    messagebox.showinfo('UPDATED','Information updated')
    
def SHOW():
    secondWindow = tk.Tk()
    secondWindow.title("Display results")
    secondWindow.resizable(width=False, height=False)
    secondWindow.geometry('{}x{}'.format(1200, 900))
    qlabel = tk.Label(secondWindow, text='TEACHER INFORAMTION', width=52, bg='grey')
    qlabel.config(font=("Sylfaen", 30))
    qlabel.pack()

    tree = ttk.Treeview(secondWindow) #treeview is used to print and allowing browsing through hierarchy of items.
    tree["columns"] = ("one", "two", "three", "four","five")

    tree.heading("one", text="teacher ID")
    tree.heading("two", text="teacher Name")
    tree.heading("three", text="College Name")
    tree.heading("four", text="Address")
    tree.heading("five", text="Phone no")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(i+1),
                    values=(row[0],row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()




mainwindow.mainloop()



    