# # from flask import Flask, render_template
# # #from markupsafe import escape

# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return render_template('home.html')

# # if __name__ == "__main__":
# #     app.run()

#from contextlib import redirect_stderr
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
  return render_template('home.html')
 
@app.route('/alarm')
def about():
    return render_template('alarm.html')

@app.route('/info')
def info():
    # return 
    return render_template('weather.html')

@app.route('/test')
def test():
    return render_template('test.html')

from urllib import parse, request
from urllib.request import urlopen
from bs4 import BeautifulSoup

# @app.route('/weather')
# def weat():

#     url = request.urlopen("https://search.naver.com/search.naver?query="+parse.quote("서울+날씨"))
#     #res = url.read()
#     soup = BeautifulSoup(url, "html.parser")
   
#     keyword_f1 = str(soup.find('span', class_='weather before_slash')).split(">")[1][:2] # '흐림'
#     keyword_f2 = soup.select_one('.temperature_text').get_text().replace('도', '도 ') # ' 현재 온도 16° '
 
#     # #print(keyword_f1)
#     # #print(keyword_f2)

#     # output = "<!DOCTYPE html><html>"
#     # output += "현재 상태 " + keyword_f1
#     # output += "<br>" + keyword_f2
#     # output += "</html>"

#     return render_template('1136test.html')

@app.route('/weather')
def weat():
    url = request.urlopen("https://search.naver.com/search.naver?query="+parse.quote("서울+날씨"))
    #res = url.read()
    soup = BeautifulSoup(url, "html.parser")
   
    keyword_f1 = str(soup.find('span', class_='weather before_slash')).split(">")[1][:2] # '흐림'
    keyword_f2 = soup.select_one('.temperature_text').get_text().replace('도', '도 ') # ' 현재 온도 16° '
    return render_template("weather.html", key1 = keyword_f1, key2 = keyword_f2)

@app.route('/video')
def video():
    return render_template('video.html')
    
@app.route('/emergency')
def emer():
    return render_template('emergency.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = "8080")

