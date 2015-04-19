#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb

def conndb():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="000000",db="jol",charset="utf8")
    cur = conn.cursor()
    cur.execute("select user_id, nick, team_telephone from users where team_id>0 ")
    team_data = []    
    for data in cur.fetchall():
        team_single = {"user_id":data[0], "nick":data[1], "team_telephone":data[2]}
        team_data.append(team_single)
    cur.close()
    return team_data
   
def test():
    print conndb()

if __name__ == '__main__':
    test()
