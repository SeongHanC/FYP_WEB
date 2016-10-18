import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="t1213121", db="User")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS USERS")

sql = """CREATE TABLE USERS(
            USERNAME CHAR(20) NOT NULL,
            PASSWORD VARCHAR(20) NOT NULL,
            STATE CHAR(20),
            LOCATION CHAR(20))
        """

cursor.execute(sql)

db.close()
