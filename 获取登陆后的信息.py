from bs4 import BeautifulSoup
import requests
import os
import codecs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Cookie': 'LUOOSESS=n932p21n1ouo91jlshoak0ng85; lult=2796450f60ec78c983f70856c41f52b5; __utmt=1; __utma=219955972.508512510.1453453690.1457348278.1457566306.12; __utmb=219955972.6.10.1457566306; __utmc=219955972; __utmz=219955972.1453453690.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}
# cookies = dict(cookies_are='working')
url_info = "http://www.luoo.net/user/"
url_music_list = "http://www.luoo.net/user/singles?p="
songs = []
singers = []
info = []
wb_data_list = ""
list_encode = ""

# 解析获得歌曲列表页数
wb_data = requests.get(url_info, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
pages = soup.select('a.page')
# print(pages[-1].text)

# 创建歌曲列表文件
list_txt = codecs.open("落网收藏歌曲列表.txt", "w", "utf-8")

# 循环解析每一页歌曲
# print(int(pages[-1].text))
for i in range(1, int(pages[-1].text) + 1):
    wb_data_list = requests.get(url_music_list + str(i), headers=headers)
    wb_data_list.encoding = 'utf-8'
    soup_list = BeautifulSoup(wb_data_list.text, 'lxml')
    songs.extend(soup_list.select('a.trackname.btn-play'))
    singers.extend(soup_list.select('span.artist.btn-play'))

# 循环写入歌曲txt
# print(songs[len(songs)-1])
# print(range(len(songs)))
for i in range(len(songs)):
    # print(songs[i].text + " - " + singers[i].text)
    data = {
        'songs': songs[i].get_text(),
        'singers': singers[i].get_text()
    }
    info.append(data)
    list_encode += '{0} - {1}\n'.format(str(songs[i].get_text()), str(singers[i].get_text()))

list_txt.write(list_encode)
print("生成完毕")
list_txt.close()
# print(info)
# 退出等待
os.system('pause')
