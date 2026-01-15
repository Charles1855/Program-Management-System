
import tkinter as tk
import sqlite3


def connect_db():
    return sqlite3.connect("mhub.db")


def open_reports_window():
    window = tk.Toplevel()
    window.title("Reports & Analytics")
    window.geometry("500x500")

    text = tk.Text(window, font=("Arial", 11))
    text.pack(fill="both", expand=True)

    conn = connect_db()
    cursor = conn.cursor()

    # Total participants
    cursor.execute("SELECT COUNT(*) FROM participants")
    total_participants = cursor.fetchone()[0]

    # Total programs
    cursor.execute("SELECT COUNT(*) FROM programs")
    total_programs = cursor.fetchone()[0]

    text.insert("end", "📊 MHUB SYSTEM REPORT\n")
    text.insert("end", "-" * 40 + "\n\n")

    text.insert("end", f"Total Participants: {total_participants}\n")
    text.insert("end", f"Total Programs: {total_programs}\n\n")

    text.insert("end", "📌 Enrollment Per Program:\n")

    cursor.execute("""
    SELECT programs.program_name, COUNT(enrollments.id)
    FROM programs
    LEFT JOIN enrollments ON programs.id = enrollments.program_id
    GROUP BY programs.id
    """)

    for program, count in cursor.fetchall():
        text.insert("end", f" - {program}: {count} enrolled\n")

    text.insert("end", "\n📌 Attendance Summary:\n")

    cursor.execute("""
    SELECT programs.program_name, attendance.status, COUNT(*)
    FROM attendance
    JOIN programs ON attendance.program_id = programs.id
    GROUP BY programs.program_name, attendance.status
    """)

    for program, status, count in cursor.fetchall():
        text.insert("end", f" - {program}: {count} {status}\n")

    conn.close()
