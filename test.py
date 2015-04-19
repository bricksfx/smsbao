#coding=utf-8
import hashlib
import urllib
import urllib2
p=hashlib.md5()
p.update("fangxubz258866")
passw = p.hexdigest()
smsapi = "api.smsbao.com"
user = "bricksfx"
phone = "13555791383"
phone = raw_input("请输入号码")

#sendurl = "http://{$smsapi}/sms?u={$user}&p={$pass}&m={$phone}&c="
sendurl = "http://%s/sms?u=%s&p=%s&m=%s&" % (smsapi, user, passw, phone)
com = raw_input("请输入短信内容")
comment = {'c':com}
data = urllib.urlencode(comment)
req = urllib2.Request(sendurl, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

