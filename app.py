# _*_ coding: utf-8 _*_
# flask run --host 0.0.0.0 --port 8080
import datetime
import random
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
    
# variable routing
@app.route("/hello/<string:name>")
def hellotak(name):
    return render_template("hello.html", n=name)

# https://~~~.c9.io/cube/숫자
# 제곱한 결과를 출력
@app.route("/cube/<int:num>")
def cube(num):
    return render_template("cube.html", n=num*num)

@app.route("/lunch")
def lunch():
    lunch_box = ["20층", "김밥카페", "양자강", "바스버거", "시골집"]
    lunch = random.choice(lunch_box)
    return render_template("lunch.html", lunch=lunch, box=lunch_box)

@app.route("/christmas")
def christmas():
    now = datetime.datetime.now()
    christmas = ""
    if now.day == 25 and now.month == 12:
        christmas = "맞아!"
    else:
        christmas = "아니야!" 
    return render_template("christmas.html", christmas=christmas)
    
@app.route('/google')
def google():
    return render_template("google.html")

@app.route('/opgg')
def opgg():
    return render_template("opgg.html")
    
@app.route('/opggresult')
def opggresult():
    name = request.args.get('q')
    url = "http://www.op.gg/summoner/userName="
    res = requests.get(url+name)
    bs = BeautifulSoup(res.content, 'html.parser')
    win = bs.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')[0].text
    lose = bs.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')[0].text
    return render_template("opggresult.html", name=name, win=win, lose=lose)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)