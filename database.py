import sqlite3

conn = sqlite3.connect("mhub.db")
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS programs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER,
        program_id INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER,
        program_id INTEGER,
        status TEXT
    )
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO users (id, username, password)
    VALUES (1, 'admin', 'admin123')
    """)

    conn.commit()
