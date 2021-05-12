from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

html=urlopen('https://movie.naver.com/movie/running/current.nhn')

soup=BeautifulSoup(html,'lxml')

movie_content=soup.find_all('div',{'id':'content'})
movie_li=movie_content[0].find_all('li')

title_list=[]
score_list=[]
movie_ranking=dict()

for data in movie_li:
    title=data.find_all('dt',{'class':'tit'})
    for content in title:
        content=content('a')
        for content2 in content:
            title_list.append(content2.get_text())

    score=data.find_all("dl",{"class":"info_star"})
    for content in score:
        content=content.find_all("span",{'class':'num'})
        for content2 in content:
            score_list.append(content2.get_text())

for i in range(len(title_list)):
    movie_ranking[str(i+1)+"위"]=title_list[i]+":"+score_list[i]

for rank,info in movie_ranking.items():
    print(rank,"-",info)

