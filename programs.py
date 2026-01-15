import tkinter as tk
import sqlite3

def screen(root, go_back):
    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="Programs", font=("Arial", 16)).pack(pady=10)

    program = tk.Entry(frame)
    program.pack()

    def save():
        conn = sqlite3.connect("mhub.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO programs VALUES (NULL, ?)", (program.get(),))
        conn.commit()
        conn.close()

    tk.Button(frame, text="Save", command=save).pack(pady=5)
    tk.Button(frame, text="Back", command=lambda: go_back(root)).pack(pady=10)
