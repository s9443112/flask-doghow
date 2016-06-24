import requests
from bs4 import BeautifulSoup
import HTMLParser
import sys
from IPython.display import clear_output
import io

lang = []
links = 'http://bahamut.com.tw/'
gamer = io.open('gamer.txt',encoding = 'utf-8', mode = 'w')

res = requests.get(links)
res.encoding = 'utf-8'
gamer.write(res.text)

gamer.close()
##----------------------------------
soup = BeautifulSoup(res.text.encode('utf-8'),'html.parser')

news_table = soup.find('div',{'id':'hothala'})
##news_table = news_table.find('table',{'class':'EXA8'})
##news_table = news_table.find_all('tr')

gamer_news_list = io.open('gamer_news_list.txt',encoding = 'utf-8',mode = 'w')
'''
for i in range(1,len(news_table)):
    try:
        num = news_table[i].find_all('span')[0].string
    except Exception as e:
        num = ""
    try:
        hola_name = news_table[i].find('a',{'class':'style2'}).string
    except Exception as e:
        hola_name = ""
    try:
        talk = news_table[i].find_all('a')[1].string
    except Exception as e:
        talk = ""

    result = num +" :   "+hola_name+" :     "+talk

    try:
        gamer_news_list.write(result + '\n')
    except Exception as e:
        print('pass')

    clear_output
    print(i)

    sys.stdout.flush()
'''
try:
    hola_name = str(news_table)
except Exception as e:
    hola_name = ""

result = hola_name

try:
    gamer_news_list.write(result + '\n')
except Exception as e:
    print('pass')
clear_output()

gamer_news_list.close()
