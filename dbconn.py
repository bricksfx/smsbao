#coding=utf8
import MySQLdb

def conndb():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="000000",db="jol",charset="utf8")
    cur = conn.cursor()
    cur.execute("select * from users")
    for data in cur.fetchall():
        print data
    cur.close()
    