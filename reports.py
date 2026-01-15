import tkinter as tk
import sqlite3

def screen(root, go_back):
    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="Reports", font=("Arial", 16)).pack(pady=10)

    conn = sqlite3.connect("mhub.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM participants")
    tk.Label(frame, text=f"Participants: {cur.fetchone()[0]}").pack()

    cur.execute("SELECT COUNT(*) FROM programs")
    tk.Label(frame, text=f"Programs: {cur.fetchone()[0]}").pack()

    conn.close()

    tk.Button(frame, text="Back", command=lambda: go_back(root)).pack(pady=20)
