#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from mesSend import mesSend
from dbconn import conndb
import time

def send_mes_to_team():
    team_data = conndb()
    fail = {}
    for team_single in team_data:
        con = unicode("于4月22下午一点在信息楼205、220举行热身赛，请回复 队号+是否到场至 13897959151 ")
        content = unicode("ACMLab") + con
        tel = team_single['team_telephone']
        sendstatus = mesSend(tel, content)
        if sendstatus != 0:
            print sendstatus
            print team_single
        time.sleep(2)

if __name__ == '__main__':
    send_mes_to_team()


