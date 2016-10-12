import MySQLdb

def connection():
    connect = MySQLdb.connect(host="localhost",user = "root",passwd = "t1213121",db = "User")
    c = connect.cursor()

    return c, connect