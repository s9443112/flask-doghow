import requests
from bs4 import BeautifulSoup
import HTMLParser
import time
from random import randint
import sys
from IPython.display import clear_output


langs = []
links = 'http://www.csie.yuntech.edu.tw/index.php'

yuntech_csie = open('yuntech_csie.txt',encoding = "utf-8",mode = "w")

res = requests.get(links)
res.encoding = 'utf-8'
yuntech_csie.write(res.text)

yuntech_csie.close()
##--------------------------------
soup = BeautifulSoup(res.text.encode("utf-8"),'html.parser')

news_table = soup.find('div',{'id':'Mod115'})
news_table = news_table.find('div',{'class':'module-content2'})
##news_table = news_table.find('div',{'class':'div_lnd_list'})
news_table = news_table.find('ul',{'class':'smartlatest'})



yuntech_news_list = open('yuntech_news_list.txt',encoding = "utf-8",mode = 'w')
count = 0
'''
for i in range(1,len(news_table)):

    try:
        new = news_table[i].find_all('li').string
        new = new.lstrip()
        print(new)
    except Exception as e:
        new = ""

    try:
        news_table = str(news_table)
    except Exception as e:
        news_table = ""

    count = count + 1
    result = news_table

    try:
       yuntech_news_list.write(result + '\n')
    except Exception as e:
       print ('pass')
    ##time.sleep(randint(1,3))
    clear_output()
    print (i)

    sys.stdout.flush()
'''
try:
    news_table = str(news_table)
except Exception as e:
    news_table = ""

count = count + 1
result = news_table

try:
   yuntech_news_list.write(result + '\n')
except Exception as e:
   print ('pass')
##time.sleep(randint(1,3))
clear_output()


sys.stdout.flush()

yuntech_news_list.close()
