import tkinter as tk
from database import cursor
from dashboard import dashboard_screen

def login_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="Login", font=("Arial", 16)).pack(pady=10)

    username = tk.Entry(frame)
    username.pack()
    username.insert(0, "admin")

    password = tk.Entry(frame, show="*")
    password.pack()
    password.insert(0, "admin123")

    def login():
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username.get(), password.get())
        )
        if cursor.fetchone():
            dashboard_screen(root)

    tk.Button(frame, text="Login", command=login).pack(pady=10)
