#from pathlib import Path
#from config import DATABASE_FILE_PATH
from database_connection import get_database_connection


#import sqlite3
#from repositories.database_connection import get_database_connection

class PlayerScoresRepository:
    #def __init__(self, connection=get_database_connection()):
    def __init__(self, connection):
        self._connection = connection
        cursor = self._connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PlayerScores (
                name TEXT PRIMARY KEY,
                wins INTEGER,
                losses INTEGER,
                draws INTEGER
            );
        """)

        connection.commit()

    def add_player(self, name):
        if not name:
            return
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM PlayerScores WHERE name=?", (name,))
        result = cursor.fetchone()
        if result:
            return

        cursor.execute("""
            INSERT INTO PlayerScores (name, wins, losses, draws) VALUES (?, ?, ?, ?)
        """, (name, 0, 0, 0))

        self._connection.commit()

    def get_names(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM PlayerScores")
        rows = cursor.fetchall()
        return [row["name"] for row in rows]

    def get_scores(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM PlayerScores")
        rows = cursor.fetchall()
        return [(row["name"], row["wins"], row["losses"], row["draws"]) for row in rows]

    def update_score(self, name, win, loss, draw):
        if not name:
            return False

        cursor = self._connection.cursor()

        cursor.execute("UPDATE PlayerScores SET wins=wins+?, "
                        "losses=losses+?, draws=draws+? WHERE name = ?",
                        (win, loss, draw, name))
        self._connection.commit()
        return True



    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from PlayerScores')
        self._connection.commit()

score_repository = PlayerScoresRepository(get_database_connection())
