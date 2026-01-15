
# Main dashboard window
import tkinter as tk
from participants import open_participant_window
from programs import open_program_window
from enrollment import open_enrollment_window
from attendance import open_attendance_window
from reports import open_reports_window


def open_dashboard(role):
    dashboard = tk.Tk()
    dashboard.title("MHub Program Management System - Dashboard")
    dashboard.geometry("400x450")
    dashboard.resizable(False, False)

    tk.Label(
        dashboard,
        text="MHub Program Management System",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Button(dashboard, text="Manage Participants", width=25, command=open_participant_window).pack(pady=10)
    tk.Button(dashboard, text="Manage Programs", width=25, command=open_program_window).pack(pady=10)
    tk.Button(dashboard, text="Enroll Participants", width=25, command=open_enrollment_window).pack(pady=10)
    tk.Button(dashboard, text="Attendance", width=25, command=open_attendance_window).pack(pady=10)
    tk.Button(dashboard, text="View Reports", width=25, command=open_reports_window).pack(pady=10)

    dashboard.mainloop()
