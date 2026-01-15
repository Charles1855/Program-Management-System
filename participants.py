# participants.py
# Participant management module

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


def connect_db():
    return sqlite3.connect("mhub.db")


def save_participant(name, gender, phone, email, location):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO participants
    (full_name, gender, phone, email, location, date_registered)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, gender, phone, email, location, datetime.now().strftime("%Y-%m-%d")))

    conn.commit()
    conn.close()


def open_participant_window():
    window = tk.Toplevel()
    window.title("Manage Participants")
    window.geometry("400x400")

    fields = ["Full Name", "Gender", "Phone", "Email", "Location"]
    entries = {}

    for field in fields:
        tk.Label(window, text=field).pack()
        entry = tk.Entry(window)
        entry.pack()
        entries[field] = entry

    def save():
        if not entries["Full Name"].get():
            messagebox.showerror("Error", "Full Name required")
            return

        save_participant(
            entries["Full Name"].get(),
            entries["Gender"].get(),
            entries["Phone"].get(),
            entries["Email"].get(),
            entries["Location"].get()
        )

        messagebox.showinfo("Success", "Participant saved")
        for e in entries.values():
            e.delete(0, tk.END)

    tk.Button(window, text="Save Participant", command=save).pack(pady=20)
