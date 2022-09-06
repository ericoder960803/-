from base64 import encode
from contextlib import redirect_stdout

import re
from unittest import result
from urllib import request
from flask import Flask,render_template,request,make_response,redirect,url_for
from crawler import crawler,article
import json

app=Flask(__name__,static_folder='/static')
app.config['JSON_AS_ASCII']= False
@app.route('/')
def hello():
    return redirect(url_for('test',page=1))

@app.route("/<int:page>")
def test(page):
    
    t=crawler.getarticle(page,20)
    
    #t=json.dumps(t,ensure_ascii=False).encode('utf8')
    return render_template("index.html",result=t,page=page)
@app.route("/api/<page>", methods=['GET'])
def api(page):
    t=crawler.getarticle(1,100000)
    return render_template()
@app.route("/post/<int:id>", methods=['GET'])
def look(id):
    a=article.getmedia(id)
    b=article.getmedi(id)
    return render_template("view.html",result=a,list=b)



    
app.run(port=4999)