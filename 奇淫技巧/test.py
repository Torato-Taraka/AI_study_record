'''
#爬取文本
from lxml import etree
import requests
url = 'https://so.gushiwen.org/shiwenv_9fedd9d41999.aspx'
xpath = '//*[@class = "contson"]//text()'
res = requests.get(url)
print(res.text)
html = etree.HTML(res.text, etree.HTMLParser())
text = html.xpath(xpath)
for i in range(len(text)):
    print(text[i])
'''

'''
#robot.txt
import urllib.robotparser as urobot
import requests
url = 'https://www.taobao.com/'
rp = urobot.RobotFileParser()
rp.set_url(url + '/robot.txt')
rp.read()
user_agent = 'Baiduspider'
if rp.can_fetch(user_agent, 'https://www.taobao.com/article/'):
    site = requests.get(url)
    print('seems good')
else:
    print('cannot scrap because robots.txt banned you!')
'''

