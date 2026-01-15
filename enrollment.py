import tkinter as tk
from database import cursor, conn

def enrollment_screen(parent):
    tk.Label(parent, text="Enrollment", font=("Arial", 14)).pack(pady=10)

    pid = tk.Entry(parent)
    pid.pack()
    pid.insert(0, "Participant ID")

    prg = tk.Entry(parent)
    prg.pack()
    prg.insert(0, "Program ID")

    def enroll():
        cursor.execute(
            "INSERT INTO enrollment (participant_id, program_id) VALUES (?, ?)",
            (pid.get(), prg.get())
        )
        conn.commit()
        pid.delete(0, tk.END)
        prg.delete(0, tk.END)

    tk.Button(parent, text="Enroll", command=enroll).pack(pady=5)
