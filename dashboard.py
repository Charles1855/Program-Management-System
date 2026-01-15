import tkinter as tk
import participants, programs, enrollment, attendance, reports

def dashboard_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    sidebar = tk.Frame(root, width=150, bg="#dddddd")
    sidebar.pack(side="left", fill="y")

    content = tk.Frame(root)
    content.pack(side="right", expand=True, fill="both")

    def load(screen_func):
        for widget in content.winfo_children():
            widget.destroy()
        screen_func(content)

    tk.Button(sidebar, text="Participants", command=lambda: load(participants.participants_screen)).pack(fill="x", pady=5)
    tk.Button(sidebar, text="Programs", command=lambda: load(programs.programs_screen)).pack(fill="x", pady=5)
    tk.Button(sidebar, text="Enrollment", command=lambda: load(enrollment.enrollment_screen)).pack(fill="x", pady=5)
    tk.Button(sidebar, text="Attendance", command=lambda: load(attendance.attendance_screen)).pack(fill="x", pady=5)
    tk.Button(sidebar, text="Reports", command=lambda: load(reports.reports_screen)).pack(fill="x", pady=5)
