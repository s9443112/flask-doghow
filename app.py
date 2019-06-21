
from flask import render_template,request,Flask
import sys
import io
import os 
import modules.crawler


app=Flask(__name__)

GoogleMaps(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/skill_tree')
def skill_tree():
    return render_template('skill_tree.html')

@app.route('/billboard',methods=['GET','POST'])
def billboard():
    take_words = ''
    words = ''
    f = io.open(os.getcwd()+'/static/text/yuntech_news_list.txt','r',encoding='utf-8')
    while True:
        words = f.readline()
        if(words==''):
            break;
        take_words=take_words+words
    f.close()

    take_game_words = ''
    game_words = ''
    f = io.open(os.getcwd()+'/static/text/gamer_news_list.txt','r',encoding='utf-8')
    while True:
        game_words = f.readline()
        if(game_words==''):
            break;
        take_game_words = take_game_words + game_words
    f.close()

    return render_template('billboard.html',take_words=take_words,take_game_words=take_game_words)


@app.route('/about')
def about():
    introduce = {'english':'Timothy','email':'s9443112@gmail.com'}
    return render_template('about.html',introduce = introduce)

@app.route('/albums')
def albums():
    return render_template('albums.html')



if __name__ == '__main__':
    app.run()
