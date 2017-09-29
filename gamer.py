import requests
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import sys
from IPython.display import clear_output
import io

langs = []
links = 'http://www.gamer.com.tw'

gamer_html = open('gamer_html.txt',encoding = "utf-8",mode = "w")

res = requests.get(links)
res.encoding = 'utf-8'
gamer_html.write(res.text)

gamer_html.close()
##-----------------------------------------------------------------------------
soup = BeautifulSoup(res.text.encode("utf-8"),'html.parser')

shop_table = soup.find('div',{'id':'hothala'})
shop_table = shop_table.find('table',{'class':'EXA8'})
shop_table = shop_table.find_all('tr')


shop_list = open('get_html.txt',encoding = "utf-8",mode = 'w')
##建立變項檔案的header
title = "排名， 哪一版， 主題， 響應 \n"
shop_list.write(title)
##先把header寫進去


for i in range(1,len(shop_table)):
    try:
        rate = shop_table[i].find_all('span')[0].string
    except Exception as e:
        rate = ""
    ##做例外處理

    try:
        board = shop_table[i].find('a',{'class':'style2'}).string
    except Exception as e:
        board = ""
    try:
        theme = shop_table[i].find_all('a')[1].string
    except Exception as e:
        theme = ""

    try:
        respo = shop_table[i].find_all('td')[3].string
    except Exception as e:
        respo = ""
    ##串起來用逗號分格（應該有更好的方法，但是先將就用用）
    result = rate + ".  " + board + "   :   " + theme + "   #    " + respo
    try:
        shop_list.write(result+'\n')
    except Exception as e:
        print ('pass')
    
    clear_output()
    print (i)

    sys.stdout.flush()

shop_list.close()