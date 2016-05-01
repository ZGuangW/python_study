from bs4 import BeautifulSoup
import requests

url = 'http://bj.58.com/pbdn/'
url2 = 'http://bj.58.com/pingbandiannao/25157105998128x.shtml?adtype=1&entinfo=25157105998128_0&psid=130006311191600633525951824&iuType=q_1'
links = []


# ===爬取每一页的所有连接===
def getPageLinks(url, links=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    page_links = soup.select('table.tbimg > tr > td.t > a')
    for i in page_links:
        if (('zhuanzhuan' not in i.get('href')) & ('e.58.com' not in i.get('href')) & (
                    'jump.zhineng.58.com' not in i.get('href'))):
            links.append(i.get('href'))


# ===爬取详细信息===
web_data = requests.get(url2)
soup = BeautifulSoup(web_data.text, 'lxml')
title = soup.select('div.col_sub.mainTitle > h1')
time = soup.select('li.time')
count = soup.select('li.count > em#totalcount')
pic = soup.select('ul#img_smalls > li > img')
# pice = soup.select('span.price.c_f50')
# assdes = soup.find('div.col_sub.sumary > ul > li > div.su_con > span')
pice = soup.select('div.col_sub.sumary > ul > li > div.su_con > span.price.c_f50')
chengse = soup.find('div', class_='sumary').ul.li.find_next_sibling().div.find_next_sibling().span
area = soup.select('div.col_sub.sumary > ul > li > div.su_con > span > a')
username = soup.select('div.col_sub.sumary > ul.suUl > li > div.fl')  # TODO 卖家是通过js获取的，这部分需要再作研究
big_pic = []
for i in range(len(pic)):
    big_pic.append(pic[i].get('src').replace('tiny', 'big'))

print(username)
