import sqlite3


class DBConnection():

    @staticmethod
    def getConnection():
        try:
            conn = sqlite3.connect("rabbitranch (copy).db")

            return conn
        except Exception as e:
            print(e)
