import sqlite3

def connect_db():
    return sqlite3.connect("mhub.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS programs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        program_name TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER,
        program_id INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER,
        program_id INTEGER,
        status TEXT
    )""")

    conn.commit()
    conn.close()
