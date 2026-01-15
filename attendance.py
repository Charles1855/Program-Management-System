import tkinter as tk
from database import cursor, conn

def attendance_screen(parent):
    tk.Label(parent, text="Attendance", font=("Arial", 14)).pack(pady=10)

    pid = tk.Entry(parent)
    pid.pack()
    pid.insert(0, "Participant ID")

    prg = tk.Entry(parent)
    prg.pack()
    prg.insert(0, "Program ID")

    def mark():
        cursor.execute(
            "INSERT INTO attendance (participant_id, program_id, status) VALUES (?, ?, 'Present')",
            (pid.get(), prg.get())
        )
        conn.commit()
        pid.delete(0, tk.END)
        prg.delete(0, tk.END)

    tk.Button(parent, text="Mark Present", command=mark).pack(pady=5)
