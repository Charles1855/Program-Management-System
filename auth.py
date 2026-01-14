import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

def connect_db():

    return sqlite3.connect("mhub.db")

def create_default_admin():
    
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    user_exists = cursor.fetchone()

    if not user_exists:
        cursor.execute("""
        INSERT INTO users (username, password, role, created_at)
        VALUES (?, ?, ?, ?)
        """, ("admin", "admin123", "Admin", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        conn.commit()

    conn.close()

def login(username, password):
    """
    Validates user credentials.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT role FROM users
    WHERE username = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()
    conn.close()

    return user

def login_window():
    """
    Displays the login window.
    """
    window = tk.Tk()
    window.title("MHub Program Management System - Login")
    window.geometry("400x300")
    window.resizable(False, False)

tk.Label(window, text="Login", font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(window, text="Username").pack()
username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Password").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        user = login(username, password)

        if user:
            messagebox.showinfo("Success", f"Welcome {user[0]}")
            window.destroy()
            # Dashboard will be loaded here later
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

tk.Button(window, text="Login", width=15, command=handle_login).pack(pady=20)

window.mainloop()
