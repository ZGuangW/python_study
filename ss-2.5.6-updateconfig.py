from bs4 import BeautifulSoup
import requests
import os
import codecs
import sys

'''
本模块适用于shadowsocks-2.5.6
Author:ZGuangW
'''
url = "http://www.ishadowsocks.com/"
info = []
configs = ""
try:
    wb_data = requests.get(url)
except BaseException:
    print("程序异常")
    os.system('pause')
    sys.exit()
wb_data.encoding = "utf-8"
soup = BeautifulSoup(wb_data.text, 'lxml')
server_sties = soup.select('#free > div > div > div > h4:nth-of-type(1)')
server_ports = soup.select('#free > div > div > div > h4:nth-of-type(2)')
passwords = soup.select('#free > div > div > div > h4:nth-of-type(3)')
methods = soup.select('#free > div > div > div > h4:nth-of-type(4)')
remakes = soup.select('#free > div > div > div > h4:nth-of-type(1)')

for server_stie, server_port, password, method, remake in zip(server_sties, server_ports, passwords, methods, remakes):
    data = {
        "server": server_stie.get_text()[server_stie.get_text().index(':') + 1:],
        "server_port": server_port.get_text()[server_port.get_text().index(':') + 1:],
        "password": password.get_text()[password.get_text().index(':') + 1:],
        "method": method.get_text()[method.get_text().index(':') + 1:],
        "remarks": remake.get_text()[:1]
    }
    info.append(data)

# 格式化配置文件
configs = '{\n"configs" : [\n  {\n"server" : "%s",\n"server_port" : %s,\n"password" : "%s",\n"method" : "%s",\n"remarks" : "%s"}\n,\n  {\n"server" : "%s",\n"server_port" : %s,\n"password" : "%s",\n"method" : "%s",\n"remarks" : "%s"}\n,\n  {\n"server" : "%s",\n"server_port" : %s,\n"password" : "%s",\n"method" : "%s",\n"remarks" : "%s"}\n\n],\n"strategy" : "com.shadowsocks.strategy.ha",\n"index" : -1,\n"global" : false,\n"enabled" : true,\n"shareOverLan" : true,\n"isDefault" : false,\n"localPort" : 1080,\n"pacUrl" : null,\n"useOnlinePac" : false,\n"availabilityStatistics" : true}' % (
info[0]["server"], info[0]["server_port"], info[0]["password"], info[0]["method"], info[0]["remarks"],
info[1]["server"], info[1]["server_port"], info[1]["password"], info[1]["method"], info[1]["remarks"],
info[2]["server"], info[2]["server_port"], info[2]["password"], info[2]["method"], info[2]["remarks"])
# print(configs)
# configs.encode(encoding='utf-8')

# 创建配置文件
list_txt = codecs.open("gui-config.json", "w", "utf-8")
list_txt.write(configs)
list_txt.close()

try:
    # 直接调用启动程序
    os.system('Shadowsocks.exe')
    print("更新并启动成功")
except BaseException:
    print("启动Shadowsocks失败")

# 退出程序
sys.exit()
