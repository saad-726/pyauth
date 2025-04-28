import tkinter as tk
from tkinter import messagebox

# Predefined admin and user credentials
u_id = "user@gmail.com"
u_password = "123"
a_id = "admin@gmail.com"
a_password = "123"

# Lists to store registered users
userID = []
userPassword = []

def register_user():
    n_id = email_entry.get()
    n_password = password_entry.get()
    
    if n_id != "" and n_password != "":
        userID.append(n_id)
        userPassword.append(n_password)
        message_label.config(text="User registered successfully!", fg="green")
    else:
        message_label.config(text="Please fill all fields.", fg="red")

def login_user():
    id = email_entry.get()
    password = password_entry.get()

    if id == u_id and password == u_password:
        message_label.config(text="Welcome, User!", fg="green")
    elif id == a_id and password == a_password:
        message_label.config(text="Welcome, Admin!", fg="blue")
    elif id in userID:
        index = userID.index(id)
        if userPassword[index] == password:
            message_label.config(text="Welcome, Registered User!", fg="green")
        else:
            message_label.config(text="Incorrect password.", fg="red")
    else:
        response = messagebox.askyesno("Not Found", "You are not registered. Do you want to register?")
        if response:
            register_user()
        else:
            message_label.config(text="Exiting...", fg="red")

# --- GUI Part ---
root = tk.Tk()
root.title("Authentication System")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Labels
tk.Label(root, text="Email:", bg="#f0f0f0").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

tk.Label(root, text="Password:", bg="#f0f0f0").pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Login", command=login_user, bg="lightblue").pack(pady=10)
tk.Button(root, text="Register", command=register_user, bg="lightgreen").pack()

# Message Label
message_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10))
message_label.pack(pady=20)

root.mainloop()
