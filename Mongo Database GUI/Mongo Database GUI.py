from tkinter import *
import tkinter.messagebox as message
from pymongo import MongoClient

client = MongoClient()

def connect():
    host = entry_host.get()
    port = entry_port.get()
    database = entry_database.get()
    collection = entry_collection.get()
    client = MongoClient("localhost", 27017)
    db = client[database]
    coll = db[collection]
    for x in coll.find():
        print(x)
    message.showinfo("Mongo Connect", "Connect")

def reset():
    client.close()
    message.showinfo("Mongo Connect", "Reset")

root = Tk()

#Row 1
label_head = Label(root, text = "Mongo Connect")
label_head.grid(row = 0, column = 1)

#Row 2
label_host = Label(root, text = "Enter host name")
label_host.grid(row = 2, column = 0)
entry_host = Entry(root)
entry_host.grid(row = 2, column = 2)

#Row 3
label_port = Label(root, text = "Enter the port")
label_port.grid(row = 3, column = 0)
entry_port = Entry(root)
entry_port.grid(row = 3, column = 2)

#Row 4
label_database = Label(root, text = "Enter your database")
label_database.grid(row = 4, column = 0)
entry_database = Entry(root)
entry_database.grid(row = 4, column = 2)

#Row 5
label_collection = Label(root, text = "Enter Collection")
label_collection.grid(row = 5, column = 0)
entry_collection = Entry(root)
entry_collection.grid(row = 5, column = 2)

#Row 6
connect = Button(root, text = "Connect", command = connect)
connect.grid(row = 6, column = 0)
reset = Button(root, text = "Reset", command = reset)
reset.grid(row = 6, column = 2)

root.mainloop()
