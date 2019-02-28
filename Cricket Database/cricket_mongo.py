import tkinter.messagebox
from tkinter import *
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
database = client.cricket
collection = database.players

def check_player_existance(name):
    player = collection.find_one({"name":name})
    if player != None:
        return True
    else:
        return False

def insert():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        high_score = int(entry_high_score.get())
        add = {"name":name, "age":age, "high_score":high_score}
        collection.insert_one(add)
        tkinter.messagebox.showinfo("Success", "Inserted Successfully!!")
    except:
        tkinter.messagebox.showinfo("Error", "Please fill all the deatail correctly")

def update():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        high_score = int(entry_high_score.get())
        update = {"name":name, "age":age, "high_score":high_score}
        collection.update_one({"name":name}, {"$set":update})
        tkinter.messagebox.showinfo("Success", "Updated Successfully!!")
    except:
        tkinter.messagebox.showinfo("Error", "Please fill all the deatail correctly")

def delete():
    try:
        name = str(entry_name.get())
        if check_player_existance(name):
            collection.delete_one({"name":name})
            tkinter.messagebox.showinfo("Success", "Deleted Successfully!!")
        else:
            tkinter.messagebox.showinfo("Error", "Player does not exist!!")
    except:
        tkinter.messagebox.showinfo("Error", "Please fill all the deatail correctly")

def show():
    player = ""
    for data in collection.find().sort("name"):
        player = player + (data["name"]+"\t"+str(int(data["age"]))+"\t"+str(int(data["high_score"]))+"\n")
    tkinter.messagebox.showinfo("Database", "Name\t\tAge\tHigh Score\n\n"+player)

root = Tk()

label_name = Label(root, text = "Player Name")
label_name.grid(row = 0, column = 0)
entry_name = Entry(root)
entry_name.grid(row = 0, column = 2)

label_age = Label(root, text = "Age")
label_age.grid(row = 1, column = 0)
entry_age = Entry(root)
entry_age.grid(row = 1, column = 2)

label_high_score = Label(root, text = "High Score")
label_high_score.grid(row = 2, column = 0)
entry_high_score = Entry(root)
entry_high_score.grid(row = 2, column = 2)

insert = Button(root, text = "Insert", command = insert)
insert.grid(row = 3, column = 0)
update = Button(root, text = "Update", command = update)
update.grid(row = 3, column = 1)
remove = Button(root, text = "Delete", command = delete)
remove.grid(row = 3, column = 2)
show = Button(root, text = "Show", command = show)
show.grid(row = 3, column = 3)

root.mainloop()
