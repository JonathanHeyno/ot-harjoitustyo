from database_connection import get_database_connection


def drop_tables(connection):
    """tyhjentää voittotietokannan

    Args:
        connection: tietokannan yhteys
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists PlayerScores;
    ''')

    connection.commit()


def create_tables(connection):
    """luo voittotietokantaan taulun

    Args:
        connection: tietokannan yhteys
    """
    cursor = connection.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS PlayerScores (
                name TEXT PRIMARY KEY,
                wins INTEGER,
                losses INTEGER,
                draws INTEGER
            );
        """)

    connection.commit()


def initialize_database():
    """alustaa tietokannan
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
