import tkinter as tk
from database import create_tables
from auth import login_screen, create_default_admin

create_tables()
create_default_admin()

root = tk.Tk()
root.geometry("600x500")
root.title("MHub Program Management System")

login_screen(root)

root.mainloop()
