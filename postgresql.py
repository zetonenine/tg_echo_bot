import psycopg2

class BD:

    def __init__(self, user="postgres", password="postgres", dbname="postgres"):
        self.connection = psycopg2.connect(
            user=user,
            password=password,
            dbname=dbname)
        self.cursor = self.connection.cursor()

    def create(self):
        commands = (
            """
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                word INTEGER NOT NULL
                )
            """
        )
        with self.connection:
            return self.cursor.execute(commands)

    def add_word(self, word):
        with self.connection:
            return self.cursor.execute("INSERT INTO words (word) VALUES (%s)", (word,))

    def show_word(self, word):
        with self.connection:
            self.cursor.execute("SELECT id FROM words WHERE word =(%s)", (word,))
            obj = self.cursor.fetchall()
            return obj