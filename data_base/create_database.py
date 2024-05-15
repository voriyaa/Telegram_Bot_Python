import sqlite3


def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS YourTableName (
                        user_id INTEGER,
                        generate_mode INTEGER,
                        history TEXT
                    )''')
    conn.commit()
    conn.close()