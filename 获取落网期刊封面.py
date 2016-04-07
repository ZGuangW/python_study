from bs4 import BeautifulSoup
import requests
import os

url_info = "http://www.luoo.net/music/"
url_img_list = "http://www.luoo.net/tag/?p="
imgs = []
journal_names = []

wb_data = requests.get(url_info)
soup = BeautifulSoup(wb_data.text, 'lxml')
# print(soup)
pages = soup.select('a.page')
# print(pages[-1].text)

print("正在运行解析，请稍等待……")
for i in range(1, int(pages[-1].text) + 1):
    print("正在解析列表，第" + str(i) + "页（共"+str(pages[-1].text)+"页）")
    wb_data_list = requests.get(url_img_list + str(i))
    # print(url_img_list + str(i))
    soup_list = BeautifulSoup(wb_data_list.text, 'lxml')
    # print(soup_list)
    imgs.extend(soup_list.select('img.cover.rounded'))
    # print(soup_list.select('img.cover.rounded'))
    journal_names.extend(soup_list.select('a.name'))

if os.path.isfile('封面下载列表.txt'):
    os.remove('封面下载列表.txt')

list_txt = open('封面下载列表.txt', 'w')

# print(imgs)
# print(len(imgs))
for i in range(len(imgs)):
    # print(journal_names[i].get_text())
    # print(imgs[i].get('src'))
    list_txt.write(imgs[i].get('src')+'\n')

list_txt.close()
# 退出等待
print("====================\n下载列表生成完成")
os.system('pause')
