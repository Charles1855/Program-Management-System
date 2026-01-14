import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

def connect_db():

    return sqlite3.connect("mhub.db")

def create_default_admin():
    
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    user_exists = cursor.fetchone()

    if not user_exists:
        cursor.execute("""
        INSERT INTO users (username, password, role, created_at)
        VALUES (?, ?, ?, ?)
        """, ("admin", "admin123", "Admin", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        conn.commit()

    conn.close()
