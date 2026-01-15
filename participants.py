import tkinter as tk
from database import cursor, conn

def participants_screen(parent):
    tk.Label(parent, text="Participants", font=("Arial", 14)).pack(pady=10)

    entry = tk.Entry(parent)
    entry.pack()

    def save():
        cursor.execute("INSERT INTO participants (name) VALUES (?)", (entry.get(),))
        conn.commit()
        entry.delete(0, tk.END)

    tk.Button(parent, text="Add Participant", command=save).pack(pady=5)
