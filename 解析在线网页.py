from bs4 import BeautifulSoup
import requests
import os

url = "http://www.ishadowsocks.com/"
info = []
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml', from_encoding="utf-8")
# print(soup.title)
server_sties = soup.select('#free > div > div > div > h4:nth-of-type(1)')
server_ports = soup.select('#free > div > div > div > h4:nth-of-type(2)')
passwords = soup.select('#free > div > div > div > h4:nth-of-type(3)')
methods = soup.select('#free > div > div > div > h4:nth-of-type(4)')
remakes = soup.select('#free > div > div > div > h4:nth-of-type(1)')


# print(soup.select('#free > div > div > div > h4'))
# print(server_sties,server_ports,passwords,methods,remakes,sep="\n======================\n")

for server_stie,server_port,password,method,remake in zip(server_sties,server_ports,passwords,methods,remakes):
    data = {
        'server_stie': server_stie.get_text()[server_stie.get_text().index(':')+1:],
        'server_port': server_port.get_text()[server_port.get_text().index(':')+1:],
        'password': password.get_text()[password.get_text().index(':')+1:],
        'method': method.get_text()[method.get_text().index(':')+1:],
        'remake': remake.get_text()[:1]
    }
    info.append(data)

for info_i in info:
    print(info_i)

os.system("pause")
