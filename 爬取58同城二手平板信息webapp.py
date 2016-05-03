from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.58.com/pbdn/'
url2 = 'http://m.58.com/gz/pingbandiannao/25878919428300x.shtml?psid=136864525191662776445085120&entinfo=25878919428300_0&iuType=p_0&PGTID=0d309654-0000-31c0-2681-0a198434ddb4&ClickID=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
}
links = []
all_data = []


# ===爬取所选页的所有连接===
def getPageLinks(url, headers, start_page, end_page, links=None):
    for one in range(start_page, end_page + 1):
        print('正在获取第%s页连接' % str(one))
        web_data = requests.get(url + 'pn' + str(one), headers=headers)
        if web_data.status_code != 200:
            print('第%s页无数据' % str(one))
            break
        soup = BeautifulSoup(web_data.text, 'lxml')
        page_links = soup.select('ul.infoList > li > a')
        if len(page_links) == 0:
            print('第%s页无数据' % str(one))
            break
        for i in page_links:
            if (('zhuanzhuan' not in i.get('href')) & ('e.58.com' not in i.get('href')) & (
                        'jump.zhineng.58.com' not in i.get('href'))):
                links.append(i.get('href'))
        if (one % 50 == 0):
            time.sleep(0.1)
        else:
            time.sleep(1)


# ===爬取详细信息===
def getPageInfo(url, headers, all_data=None):
    web_data = requests.get(url, headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select('div.title_area.bbOnepx > div.left_tit > h1')
    meta_taglist = soup.select('div.meta-taglist > span.meta-tag')
    rel_time = soup.select('div.attr_other > div.date')
    count = soup.select('div.attr_other > div.count > lable#totalcount')
    pic = soup.select('div.pictureBox > div > ul > li > img')
    price = soup.select('div.price-location > div.price')
    price_pre = soup.select('div.price-location > div.price > span.price_pre')
    address = soup.select('div.price-location > div.location > a.icon-location.icon')
    desc = soup.select('div.good_detail > div.detail_param > p.desc')
    username = soup.select('div.person_area > div.person_detail > div > p.pname')
    meta_taglist_temp = []
    pic_temp = []
    for i in meta_taglist:
        meta_taglist_temp.append(i.get_text(strip=True))
    for i in pic:
        pic_temp.append(i.get('ref'))
    data = {
        'title': title[0].get_text(strip=True),
        'meta_taglist': meta_taglist_temp,  # todo 将列表嵌入到字典无法，有待修改
        'rel_time': rel_time[0].get_text(strip=True)[4:],
        'count': count[0].get_text(),
        'pic': pic_temp,
        'price': price[0].get_text(strip=True).split('元')[0],
        'price_pre': price_pre[0].get_text(strip=True).split('元')[0],
        'address': address[0].get_text(strip=True),
        'desc': desc[0].get_text().split('  ')[1],
        'username': username[0].get_text(strip=True)
    }
    all_data.append(data)

if __name__ == '__main__':
    # getPageLinks(url, headers, 1, 1, links)
    # print(links)
    # print(len(links))

    getPageInfo(url2, headers,all_data)
    print(all_data)
