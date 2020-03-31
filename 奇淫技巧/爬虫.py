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


#爬取文本
from lxml import etree
import requests
url = 'http://m.app.caixin.com/m_topic_detail/1473.html'
xpath1 = '//*[@class = "list-box"]//a//@href'
res = requests.get(url)
#print(res.text)
html = etree.HTML(res.text, etree.HTMLParser())
urls = html.xpath(xpath1)
urls = set(urls)
urls = list(urls)

xpath2 = '//*[@class = "text"]//text()'
x = 0
for i in range(len(urls)):
    if 'china' in urls[i] or 'international' in urls[i]:
        x += 1
        f = open('news/{0}.txt'.format(x), 'w')
        print(urls[i])
        url_new = urls[i]
        res_new = requests.get(url_new)
        html_new = etree.HTML(res_new.text, etree.HTMLParser())
        text = html_new.xpath(xpath2)
        for k in range(len(text)):
            new_text = text[k].split('\u3000\u3000')
            for j in range(len(new_text)):
                if '\r\n' not in new_text[j] and '\u3000\u3000' not in new_text[j] and len(new_text[j]) > 0:
                    print(new_text[j].encode("gbk", 'ignore').decode("gbk", "ignore"), file = f)
        f.close()


        
        
        

