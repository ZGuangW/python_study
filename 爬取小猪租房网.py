'''
本模块抓取小猪短租房信息
xiaozhu.com
作者：zguang.w
'''
from bs4 import BeautifulSoup
import requests
import time

pageUrl = "http://bj.xiaozhu.com/search-duanzufang-p{}-0/"
infoUrlList = []
info_data = []


# ===获取列表===
def getInfoUrlList(pageUrl, infoUrlList=None):
    pages = int(input('请输入需要解析的页数：'))
    pageUrlList = [pageUrl.format(str(i + 1)) for i in range(pages)]
    for i in pageUrlList:
        web_data = requests.get(i)
        soup = BeautifulSoup(web_data.text, 'lxml')
        lists = soup.select('ul.pic_list.clearfix > li > a')
        for i in lists:
            list = i.get('href')
            print(list)
            infoUrlList.append(list)
            print(infoUrlList)
        time.sleep(2)
    return infoUrlList


# ===租房详细信息===
def getZufangInfo(infoUrl):
    web_data = requests.get(infoUrl)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select('span.pr5')
    dailyRents = soup.select('div.day_l > span')
    housePhotos = soup.select('ul.detail-thumb-nav > li > img')
    landlords = soup.select('a.lorder_name')
    landlordsex = soup.select('div.member_pic > div')
    landlordpic = soup.select('div.member_pic > a > img')
    housePhotosUrl = []
    for i in housePhotos:
        housePhotosUrl.append(i.get('data-bigimg'))
    data = {
        'title': titles[0].get_text(),
        'address': address[0].get_text().strip(),
        'dailyRents': dailyRents[0].get_text(),
        'housePhoto': housePhotosUrl,
        'landlords': landlords[0].get_text(),
        'landlordsex': landlordsex[0].get('class')[0] == "member_ico" if "男" else"女",
        'landlordpic': landlordpic[0].get('src')
    }
    return data


# ===获取所有租房信息===
def getAllZufangInfo(pageUrl, infoUrlList=None, info_data=None):
    infoUrlList = getInfoUrlList(pageUrl, infoUrlList=None)
    for i in infoUrlList:
        info_data.append(getZufangInfo(i))
        time.sleep(1)


if __name__ == '__main__':
    getAllZufangInfo(pageUrl,infoUrlList,info_data)
    print(info_data)
