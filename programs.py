# programs.py
# Program management module

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


def connect_db():
    return sqlite3.connect("mhub.db")


def save_program(name, desc, start, end, facilitator):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO programs
    (program_name, description, start_date, end_date, facilitator, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, desc, start, end, facilitator, datetime.now().strftime("%Y-%m-%d")))

    conn.commit()
    conn.close()


def open_program_window():
    window = tk.Toplevel()
    window.title("Manage Programs")
    window.geometry("400x450")

    fields = ["Program Name", "Description", "Start Date", "End Date", "Facilitator"]
    entries = {}

    for field in fields:
        tk.Label(window, text=field).pack()
        entry = tk.Entry(window)
        entry.pack()
        entries[field] = entry

    def save():
        if not entries["Program Name"].get():
            messagebox.showerror("Error", "Program Name required")
            return

        save_program(
            entries["Program Name"].get(),
            entries["Description"].get(),
            entries["Start Date"].get(),
            entries["End Date"].get(),
            entries["Facilitator"].get()
        )

        messagebox.showinfo("Success", "Program saved")
        for e in entries.values():
            e.delete(0, tk.END)

    tk.Button(window, text="Save Program", command=save).pack(pady=20)
