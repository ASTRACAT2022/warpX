import sqlite3

class Database:
    def __init__(self, db_path="warpgen.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def add_user(self, telegram_id):
        self.cursor.execute("INSERT OR IGNORE INTO users (telegram_id) VALUES (?)", (telegram_id,))
        self.conn.commit()
