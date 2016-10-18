import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="t1213121", db="User")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS HISTORY")

sql = """CREATE TABLE HISTORY(
            TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            STATE CHAR(20),
            SERVICE CHAR(20))
        """

cursor.execute(sql)

db.close()