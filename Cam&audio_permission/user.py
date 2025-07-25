from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
users_collection = db["users"]


def save_user():
    user_details = {
        "name": name_entry.get(),
        "email": email_entry.get(),
        "age": int(age_entry.get())
    }
    users_collection.insert_one(user_details)
    messagebox.showinfo("Success", "User details saved successfully!")


# Create the GUI
root = tk.Tk()
root.title("User Details Form")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(root, text="Save User Details", command=save_user).pack()

root.mainloop()
