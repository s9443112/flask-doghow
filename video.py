import requests
from bs4 import BeautifulSoup
import HTMLParser
import time
from random import randint
import sys
from IPython.display import clear_output
import io

langs = []
links = 'http://2d-gate.org/thread-12871-1-1.html#.V2uh2bh96hc'

video_2d_gate = io.open('2d_gate.txt',encoding = 'utf-8',mode = 'w')

res = requests.get(links)
res.encoding = 'utf-8'
video_2d_gate.write(res.text)

video_2d_gate.close()
##--------------------------------
soup = BeautifulSoup(res.text.encode('utf-8'),'html.parser')

news_table = soup.find('div',{'class':'shadowbox'})
news_table = news_table.find('div',{'class':'wp cl'})
news_table = news_table.find('div',{'id':'postlist'})
news_table = news_table.find('div',{'class':'t_fsz'})



##news_table = news_table.find('div',{'id':'tab-6caf73-0'})

'''
news_table = news_table.find('div',{'class':'module-content2'})
##news_table = news_table.find('div',{'class':'div_lnd_list'})
news_table = news_table.find('ul',{'class':'smartlatest'})
news_table = news_table.find_all('li',{'class':'smartlatest-newsli'})


2d_gate_get = open('yuntech_news_list.txt',encoding = "utf-8",mode = 'w')
count = 0
for i in range(1,len(news_table)):
    try:
        new = news_table[i].find('a',{'class':'smartlatest-title-link'}).string
        new = new.lstrip()
    except Exception as e:
        new = ""
    try:
        data = news_table[i].find('div',{'class':'smartlatest-date'}).string
        data = data.lstrip()
    except Exception as e:
        data = ""

    count = count + 1
    result = str(count)+" : " + new + " , " + data

    try:
       2d_gate_get.write(result + '\n')
    except Exception as e:
       print ('pass')
    ##time.sleep(randint(1,3))
    clear_output()
    print (i)

    sys.stdout.flush()

2d_gate_get.close()
'''

video_2d_gate_get = io.open('video_2d_gate_get.txt',encoding = 'utf-8',mode = 'w')
try:
    news_table = str(news_table)
except Exception as e:
    news_table = ""


result = news_table

try:
   video_2d_gate_get.write(result + '\n')
except Exception as e:
   print ('pass')
##time.sleep(randint(1,3))
clear_output()


sys.stdout.flush()
video_2d_gate_get.close()
