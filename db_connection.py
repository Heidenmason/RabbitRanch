import sqlite3


class DBConnection:

    @staticmethod
    def get_connection():
        try:
            conn = sqlite3.connect("rabbitranch (copy).db")

            return conn
        except Exception as e:
            print(e)
