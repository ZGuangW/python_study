from bs4 import BeautifulSoup
import requests
import sys
import chardet
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Cookie': 'LUOOSESS=n932p21n1ouo91jlshoak0ng85; lult=2796450f60ec78c983f70856c41f52b5; __utmt=1; __utma=219955972.508512510.1453453690.1457348278.1457566306.12; __utmb=219955972.6.10.1457566306; __utmc=219955972; __utmz=219955972.1453453690.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}
# cookies = dict(cookies_are='working')
url_info = "http://www.luoo.net/user/"
wb_data = requests.get(url_info,headers = headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
print(soup)
typeEncode = sys.getfilesystemencoding()##系统默认编码
infoencode = chardet.detect(wb_data).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
# html = wb_data.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
# print(html)
# os.system("pause")
print(typeEncode,infoencode,cep='\n')