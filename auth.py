# auth.py
# User authentication module

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
from dashboard import open_dashboard


def connect_db():
    return sqlite3.connect("mhub.db")


def create_default_admin():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    if not cursor.fetchone():
        cursor.execute("""
        INSERT INTO users (username, password, role, created_at)
        VALUES (?, ?, ?, ?)
        """, ("admin", "admin123", "Admin", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()

    conn.close()


def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT role FROM users
    WHERE username = ? AND password = ?
    """, (username, password))

    result = cursor.fetchone()
    conn.close()
    return result


def login_window():
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
        user = login(username_entry.get(), password_entry.get())
        if user:
            messagebox.showinfo("Success", "Login successful")
            window.destroy()
            open_dashboard(user[0])
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(window, text="Login", command=handle_login).pack(pady=20)
    window.mainloop()
