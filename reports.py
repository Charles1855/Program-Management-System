import tkinter as tk
from database import cursor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def reports_screen(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    tk.Label(parent, text="Reports & Analytics", font=("Arial", 16)).pack(pady=10)

    # ======================
    # DATA COLLECTION
    # ======================
    cursor.execute("SELECT COUNT(*) FROM participants")
    total_participants = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM programs")
    total_programs = cursor.fetchone()[0]

    cursor.execute("""
        SELECT programs.name, COUNT(enrollment.id)
        FROM programs
        LEFT JOIN enrollment ON programs.id = enrollment.program_id
        GROUP BY programs.name
    """)
    enrollment_data = cursor.fetchall()

    # ======================
    # SUMMARY LABELS
    # ======================
    summary = tk.Frame(parent)
    summary.pack(pady=10)

    tk.Label(summary, text=f"Total Participants: {total_participants}", font=("Arial", 12)).pack(side="left", padx=20)
    tk.Label(summary, text=f"Total Programs: {total_programs}", font=("Arial", 12)).pack(side="left", padx=20)

    # ======================
    # BAR CHART
    # ======================
    bar_frame = tk.Frame(parent)
    bar_frame.pack(side="left", fill="both", expand=True)

    fig1 = Figure(figsize=(4, 3))
    ax1 = fig1.add_subplot(111)
    ax1.bar(["Participants", "Programs"], [total_participants, total_programs])
    ax1.set_title("System Overview")

    canvas1 = FigureCanvasTkAgg(fig1, bar_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(fill="both", expand=True)

    # ======================
    # PIE CHART
    # ======================
    pie_frame = tk.Frame(parent)
    pie_frame.pack(side="right", fill="both", expand=True)

    program_names = [row[0] for row in enrollment_data]
    counts = [row[1] for row in enrollment_data]

    fig2 = Figure(figsize=(4, 3))
    ax2 = fig2.add_subplot(111)

    if counts and sum(counts) > 0:
        ax2.pie(counts, labels=program_names, autopct="%1.1f%%")
    else:
        ax2.text(0.5, 0.5, "No Enrollment Data", ha="center", va="center")

    ax2.set_title("Enrollment Distribution")

    canvas2 = FigureCanvasTkAgg(fig2, pie_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(fill="both", expand=True)
