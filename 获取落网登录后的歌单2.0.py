from bs4 import BeautifulSoup
import requests
import os
import codecs
import time

url_info = 'http://www.luoo.net/user/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Cookie': 'LUOOSESS=n932p21n1ouo91jlshoak0ng85; lult=2796450f60ec78c983f70856c41f52b5; __utmt=1; __utma=219955972.508512510.1453453690.1457348278.1457566306.12; __utmb=219955972.6.10.1457566306; __utmc=219955972; __utmz=219955972.1453453690.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}
songs = []
singers = []
list_data = []
list_encode = ""


# 解析获得歌曲列表页数
def getMusicUrlList(url_info, headers):
    wb_data = requests.get(url_info, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    pages = soup.select('a.page')
    url_music_list = ['http://www.luoo.net/user/singles?p={}'.format(str(i.text)) for i in pages]
    print("列表共{}页".format(str(pages[-1].text)))
    return url_music_list


# 解析收藏列表
def getMusicList(url_music_list, headers, data=None):
    wb_data_list = requests.get(url_music_list, headers=headers)
    wb_data_list.encoding = 'utf-8'
    soup_list = BeautifulSoup(wb_data_list.text, 'lxml')
    songs = soup_list.select('a.trackname.btn-play')
    singers = soup_list.select('span.artist.btn-play')
    for song, singer in zip(songs, singers):
        data = {
            'song': song.get_text(),
            'singer': singer.get_text()
        }
        list_data.append(data)
        # print(data)
    # 增加延迟，防止ip被网站封锁
    time.sleep(2)
    return list_data


# 创建歌曲列表文件
def CreatMusicListText(list_data, list_encode):
    list_txt = codecs.open("落网收藏歌曲列表.kgl", "w", "utf-8")
    # 循环写入歌曲txt
    for i in list_data:
        list_encode += '{0} - {1}\n'.format(str(i['song']), str(i['singer']))
    list_txt.write(list_encode)
    print("列表生成完毕")
    list_txt.close()

def main():
    url_music_list = getMusicUrlList(url_info, headers)
    print("正在解析，请稍等……")
    for url in url_music_list:
        list_data = getMusicList(url, headers)
    CreatMusicListText(list_data, list_encode)

main()
# 退出等待
os.system('pause')
