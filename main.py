import tkinter as tk
from database import create_tables
from auth import login_screen

root = tk.Tk()
root.title("MHub Program Management System")
root.geometry("600x400")

create_tables()
login_screen(root)

root.mainloop()
