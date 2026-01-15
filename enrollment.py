import tkinter as tk
import sqlite3

def screen(root, go_back):
    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="Enrollment", font=("Arial", 16)).pack(pady=10)

    pid = tk.Entry(frame)
    pid.pack()
    progid = tk.Entry(frame)
    progid.pack()

    def enroll():
        conn = sqlite3.connect("mhub.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO enrollments VALUES (NULL, ?, ?)",
                    (pid.get(), progid.get()))
        conn.commit()
        conn.close()

    tk.Button(frame, text="Enroll", command=enroll).pack(pady=5)
    tk.Button(frame, text="Back", command=lambda: go_back(root)).pack(pady=10)
