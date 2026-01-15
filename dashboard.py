import tkinter as tk
import participants, programs, enrollment, attendance, reports

def dashboard_screen(root):
    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="MHub Dashboard", font=("Arial", 16)).pack(pady=20)

    tk.Button(frame, text="Participants", width=25,
              command=lambda: participants.screen(root, dashboard_screen)).pack(pady=5)

    tk.Button(frame, text="Programs", width=25,
              command=lambda: programs.screen(root, dashboard_screen)).pack(pady=5)

    tk.Button(frame, text="Enrollment", width=25,
              command=lambda: enrollment.screen(root, dashboard_screen)).pack(pady=5)

    tk.Button(frame, text="Attendance", width=25,
              command=lambda: attendance.screen(root, dashboard_screen)).pack(pady=5)

    tk.Button(frame, text="Reports", width=25,
              command=lambda: reports.screen(root, dashboard_screen)).pack(pady=5)

    tk.Button(frame, text="Exit", width=25, command=root.destroy).pack(pady=20)
