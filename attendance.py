# attendance.py
# Attendance management module

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


def connect_db():
    return sqlite3.connect("mhub.db")


def open_attendance_window():
    window = tk.Toplevel()
    window.title("Attendance")
    window.geometry("450x400")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, program_name FROM programs")
    programs = cursor.fetchall()
    conn.close()

    program_var = tk.StringVar()
    tk.Label(window, text="Program").pack()
    tk.OptionMenu(window, program_var, *[p[1] for p in programs]).pack()

    frame = tk.Frame(window)
    frame.pack(pady=10)

    def load():
        for w in frame.winfo_children():
            w.destroy()

        program_id = next(p[0] for p in programs if p[1] == program_var.get())

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT participants.id, participants.full_name
        FROM enrollments
        JOIN participants ON enrollments.participant_id = participants.id
        WHERE enrollments.program_id = ?
        """, (program_id,))
        people = cursor.fetchall()
        conn.close()

        for pid, name in people:
            var = tk.StringVar(value="Present")

            tk.Label(frame, text=name).pack(anchor="w")
            tk.Radiobutton(frame, text="Present", variable=var, value="Present").pack(anchor="w")
            tk.Radiobutton(frame, text="Absent", variable=var, value="Absent").pack(anchor="w")

            def save(p=pid, v=var):
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO attendance (participant_id, program_id, date, status)
                VALUES (?, ?, ?, ?)
                """, (p, program_id, datetime.now().strftime("%Y-%m-%d"), v.get()))
                conn.commit()
                conn.close()

            tk.Button(frame, text="Save", command=save).pack(pady=5)

    tk.Button(window, text="Load Participants", command=load).pack(pady=10)
