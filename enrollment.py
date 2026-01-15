# enrollment.py
# Participant enrollment module

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


def connect_db():
    return sqlite3.connect("mhub.db")


def open_enrollment_window():
    window = tk.Toplevel()
    window.title("Enroll Participant")
    window.geometry("400x300")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, full_name FROM participants")
    participants = cursor.fetchall()

    cursor.execute("SELECT id, program_name FROM programs")
    programs = cursor.fetchall()
    conn.close()

    tk.Label(window, text="Participant").pack()
    participant_var = tk.StringVar()
    tk.OptionMenu(window, participant_var, *[p[1] for p in participants]).pack()

    tk.Label(window, text="Program").pack()
    program_var = tk.StringVar()
    tk.OptionMenu(window, program_var, *[p[1] for p in programs]).pack()

    def enroll():
        pid = next(p[0] for p in participants if p[1] == participant_var.get())
        prid = next(p[0] for p in programs if p[1] == program_var.get())

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO enrollments (participant_id, program_id, enroll_date)
        VALUES (?, ?, ?)
        """, (pid, prid, datetime.now().strftime("%Y-%m-%d")))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Enrollment successful")

    tk.Button(window, text="Enroll", command=enroll).pack(pady=20)
