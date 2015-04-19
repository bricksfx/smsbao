#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from mesSend import mesSend
from dbconn import conndb

def send_mes_to_team():
    team_data = conndb()
    for team_single in team_data:
        content = unicode("from acmlib") + u' ' + team_single['user_id'] +unicode(" 的队长") + unicode("我们将于明天开始热身赛请做好准备")
        tel = team_single['team_telephone']
        print content
        sendstatus = mesSend(tel, content)
        if sendstatus != 0:
            print "短信发送出现错误"
            

if __name__ == '__main__':
    send_mes_to_team()


