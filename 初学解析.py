from bs4 import BeautifulSoup
import os

info = []
with open('C:/Users/w_zg/OneDrive/Project/Python/python_study/Sample1.html', 'r') as wb_date:
    Soup = BeautifulSoup(wb_date, 'lxml')
    images = Soup.select('body > div.modal-content > ul > li > img')
    titles = Soup.select('body > div.modal-content > ul > li > h3')
    descs = Soup.select('body > div.modal-content > ul > li > p')
    # print(images,titles,descs,sep='\n==================\n')

for image, title, desc in zip(images, titles, descs):
    data = {
        'image':image.get('src'),
        'title':title.get_text(),
        'desc':title.get_text()
    }
    # print(data)
    info.append(data)

print(info[0]['image'])


