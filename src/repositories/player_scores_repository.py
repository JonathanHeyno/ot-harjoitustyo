from database_connection import get_database_connection

class PlayerScoresRepository:
    """repositoryluokka voittotietokannalle
    """
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
        """lisää uuden pelaajan nimen voittotietokantaan

        Args:
            lisättävän pelaajan nimi
        """
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
        """hakee listan voittotietokannassa olevien pelaajien niistä

        Returns:
            lista voittotietokannassa olevien pelaajien nimistä
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM PlayerScores")
        rows = cursor.fetchall()
        return [row["name"] for row in rows]

    def get_scores(self):
        """hakee tietokannassa olevat voittotilastot

        Returns:
            lista kaikkien pelaajien voitoista, tappioista ja tasapeleistä
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM PlayerScores")
        rows = cursor.fetchall()
        return [(row["name"], row["wins"], row["losses"], row["draws"]) for row in rows]

    def update_score(self, name, win, loss, draw):
        """päivittää pelaajan voittotilastot kannassa

        Args:
            name: pelaajan nimi
            win: voittoihin lisättävä määrä
            loss: tappioihin lisättävä määrä
            draw: tasapeleihin lisättävä määrä

        Returns:
            boolean lisäyksen onnistumisesta
        """
        if not name:
            return False

        cursor = self._connection.cursor()

        cursor.execute("UPDATE PlayerScores SET wins=wins+?, "
                        "losses=losses+?, draws=draws+? WHERE name = ?",
                        (win, loss, draw, name))
        self._connection.commit()
        return True



    def delete_all(self):
        """poistaa kaikki tiedot kannasta
        """
        cursor = self._connection.cursor()
        cursor.execute('delete from PlayerScores')
        self._connection.commit()

score_repository = PlayerScoresRepository(get_database_connection())
