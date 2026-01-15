import tkinter as tk
import sqlite3

def connect_db():
    return sqlite3.connect("mhub.db")

def create_default_admin():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users VALUES (NULL,'admin','admin123')")
    conn.commit()
    conn.close()

def login_screen(root):
    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="Login", font=("Arial", 16)).pack(pady=10)

    username = tk.Entry(frame)
    password = tk.Entry(frame, show="*")

    tk.Label(frame, text="Username").pack()
    username.pack()

    tk.Label(frame, text="Password").pack()
    password.pack()

    def login():
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username.get(), password.get())
        )
        if cur.fetchone():
            from dashboard import dashboard_screen  # ✅ SAFE import
            dashboard_screen(root)
        conn.close()

    tk.Button(frame, text="Login", width=20, command=login).pack(pady=20)
