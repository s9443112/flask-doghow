import requests
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import time
from random import randint
import sys
from IPython.display import clear_output
import io

def yuntech_csie():
    
    langs = []
    links = 'http://www.csie.yuntech.edu.tw/index.php'

    yuntech_csie = io.open('/static/text/yuntech_csie.txt','w',encoding = 'utf-8')

    res = requests.get(links)
    res.encoding = 'utf-8'
    yuntech_csie.write(res.text)

    yuntech_csie.close()
    ##--------------------------------
    soup = BeautifulSoup(res.text.encode('utf-8'),'html.parser')

    news_table = soup.find('div',{'id':'Mod115'})
    news_table = news_table.find('div',{'class':'module-content2'})
    ##news_table = news_table.find('div',{'class':'div_lnd_list'})
    news_table = news_table.find('ul',{'class':'smartlatest'})



    yuntech_news_list = io.open('yuntech_news_list.txt','w',encoding = 'utf-8')
    count = 0

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

def gamer():
    langs = []
    links = 'http://www.gamer.com.tw'

    gamer_html = open('/static/text/gamer_html.txt',encoding = "utf-8",mode = "w")

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


if __name__ == "__main__":
    pass