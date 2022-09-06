
from unittest import result
from urllib import response
import requests as req
import bs4
from bs4 import BeautifulSoup
import lxml
class crawler():
 
 def getarticle(pag,length):
  url=f"https://www.bc3ts.com/home/newlyPostList?page={pag}&length={length}"
  responce=req.get(url)
  
  soup=bs4.BeautifulSoup(responce.content,"lxml")
  module=soup.find_all('div',class_="col-md-4")
  result=[]
  for mod in module:
    #print(title=mod.a.get('title'))
    result.append(dict(title=mod.a.get('title'),date=mod.a.find('div',class_="clearfix").small.get_text(),source=mod.a.span.get_text(),link='http://127.0.0.1:5000' + str(mod.a.get('href'))))
  return result
  #'https://www.bc3ts.com/'






class article():
  def getmedia(inturl):
    result=[]
    url= "https://www.bc3ts.com/"+str(inturl)
    responce=req.get(url)
    soup=bs4.BeautifulSoup(responce.content,'lxml')
    
    
    titleword=soup.find("h1")
    author=soup.find('span',class_="author mr-2").get_text()
    time=soup.find('span',class_="date mr-2").get_text()
    
    content_all=soup.find('div',class_="post-html")
    img=content_all.find_all("img")
    content=content_all.get_text()
    list=[]
    dic={}
    o=0
    for img in img:
      o+=1
      
      list.append(img)
    
    #for i in range(o):
      #dic[i]=list[i]
    
    try:
      yt=soup.find('iframe').get('src')
      result.append(dict(yt=yt))
    
      
    except:
      pass
    
    #print()
    #print(title,time,author,img)
    result.append(dict(title=str(titleword),author=author,time=time,content=content))
    return result
  def getmedi(inturl):
    result=[]
    url= "https://www.bc3ts.com/"+str(inturl)
    responce=req.get(url)
    soup=bs4.BeautifulSoup(responce.content,'lxml')
    
    #title=soup.find('div',class_="post-title").h1.get_text().encode("ascii", "ignore").decode()
    author=soup.find('span',class_="author mr-2").get_text()
    time=soup.find('span',class_="date mr-2").get_text()
    
    content_all=soup.find('div',class_="post-html")
    img=content_all.find_all("img")
    content=content_all.get_text()
    list=[]
    dic={}
    o=0
    for img in img:
      o+=1
      #print(img)
      list.append(img)
    
    #for i in range(o):
      #dic[i]=list[i]
    #print(dic)
    try:
      yt=soup.find('iframe').get('src')
      result.append(dict(yt=yt))
    
      
    except:
      pass
    
    #print()
    #print(title,time,author,img)
    
    return list 
    

    
      
 
      
      
  





