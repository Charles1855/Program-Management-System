import tkinter as tk
from database import cursor

def reports_screen(parent):
    tk.Label(parent, text="Reports", font=("Arial", 14)).pack(pady=10)

    cursor.execute("SELECT COUNT(*) FROM participants")
    participants = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM programs")
    programs = cursor.fetchone()[0]

    tk.Label(parent, text=f"Total Participants: {participants}").pack()
    tk.Label(parent, text=f"Total Programs: {programs}").pack()
