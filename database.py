import sqlite3

def connect_db():
    return sqlite3.connect("mhub.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        gender TEXT,
        phone TEXT,
        email TEXT,
        location TEXT,
        date_registered TEXT NOT NULL
    )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS programs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        program_name TEXT NOT NULL,
        description TEXT,
        start_date TEXT,
        end_date TEXT,
        facilitator TEXT,
        created_at TEXT NOT NULL
    )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER,
        program_id INTEGER,
        enroll_date TEXT NOT NULL,
        FOREIGN KEY (participant_id) REFERENCES participants(id),
        FOREIGN KEY (program_id) REFERENCES programs(id)
    )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER,
        program_id INTEGER,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (participant_id) REFERENCES participants(id),
        FOREIGN KEY (program_id) REFERENCES programs(id)
    )
    """)

conn.commit()
conn.close()