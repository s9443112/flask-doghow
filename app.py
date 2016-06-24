
from flask import render_template,request,Flask
import sys
import yuntech_csie
import gamer
import video
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

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
    f = open('yuntech_news_list.txt','r',encoding='utf-8')
    while True:
        words = f.readline()
        if(words==''):
            break;
        take_words=take_words+words
    f.close()
    #print(take_words)
    take_game_words = ''
    game_words = ''
    f = open('gamer_news_list.txt','r',encoding='utf-8')
    while True:
        game_words = f.readline()
        if(game_words==''):
            break;
        take_game_words = take_game_words + game_words
    f.close()
    return render_template('billboard.html',take_words=take_words,take_game_words=take_game_words)

@app.route('/video',methods=['GET','POST'])
def video():
    take_video = ''
    video = ''
    f = open('video_2d_gate_get.txt','r',encoding='utf-8')
    while True:
        video = f.readline()
        if(video==''):
            break;
        take_video=take_video+video
    f.close()

    return render_template('video.html',take_video=take_video)

@app.route('/about')
def about():
    introduce = {'chinese':'李品皜','english':'Timothy','email':'s9443112@gmail.com'}
    return render_template('about.html',introduce = introduce)

@app.route('/albums')
def albums():
    return render_template('albums.html')

@app.route('/googlemap')
def mapdemo():
    # creating a map in the view
    '''
    flaskmap = Map(
        identifier="test",
        lat=23.696167,
        lng=-120.533995,
        markers=[(23.696167, 120.533995)],
        style="width:50%;height:50%;"
    )
    return render_template('map.html',mymap=flaskmap)'''
    return render_template('map.html')

if __name__ == '__main__':
    app.run()
