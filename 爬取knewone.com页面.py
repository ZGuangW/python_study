'''
本模块爬取knewone.com产品列表
https://knewone.com/
作者：zguang.w
'''
from bs4 import BeautifulSoup
import requests
import time
import codecs

url = 'https://knewone.com/discover?page='
all_data = []
txt_temp = ""


# ===获取每页商品信息===
def get_page(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    imgs = soup.select('a.cover-inner > img')
    links = soup.select('a.cover-inner')
    titles = soup.select('h4.title > a')
    page_data = []
    for img, link, title in zip(imgs, links, titles):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'link': 'http://knewone.com' + link.get('href')
        }
        # print(data)
        page_data.append(data)
    return page_data


# ===因为不知道到底有多少页，自定义页码数===
def get_more_pages(start, end):
    for one in range(start, end + 1):
        print('正在解析第%s页' % str(one))
        all_data.extend(get_page(url + str(one)))
        if (one % 50 == 0):
            time.sleep(10)
        else:
            time.sleep(1)


# ===写入记录文档===
def writeIntoText(data, file_name=None, txt_temp=None):
    file_name = "knewone产品列表" + file_name + ".txt"
    txt = codecs.open(file_name, "w", "utf-8")
    for i in data:
        txt_temp += str(i) + "\n"
    txt.write(txt_temp)
    txt.close()
    print("生成完毕")


if __name__ == '__main__':
    start = int(input('请输入起始页：'))
    end = int(input('请输入结束页：'))
    file_name = str(input('请输入文件标识名：'))
    get_more_pages(start, end)
    writeIntoText(all_data, file_name, txt_temp)
    # print(all_data)
