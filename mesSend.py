#coding=utf8
import urllib2
import urllib
import hashlib

def mesSend(phone, message):
    p = hashlib.md5()
    p.update("fangxubz258866")
    passwd = p.hexdigest()
    user = "bricksfx"
    smsapi = "api.smsbao.com"
    sendurl = "http://%s/sms?u=%s&p=%s&m=%s&" % (smsapi, user, passwd, phone)
    comment = {'c': message}
    data = urllib.urlencode(comment)
    req = urllib2.Request(sendurl, data)
    response = urllib2.urlopen(req)
    return response.read()

def test():
    print mesSend("13555791383", "test")

if __name__ == '__main__':
    test()



