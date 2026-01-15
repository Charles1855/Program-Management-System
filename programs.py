import tkinter as tk
from database import cursor, conn

def programs_screen(parent):
    tk.Label(parent, text="Programs", font=("Arial", 14)).pack(pady=10)

    entry = tk.Entry(parent)
    entry.pack()

    def save():
        cursor.execute("INSERT INTO programs (name) VALUES (?)", (entry.get(),))
        conn.commit()
        entry.delete(0, tk.END)

    tk.Button(parent, text="Add Program", command=save).pack(pady=5)
