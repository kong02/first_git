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

#학생 2

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
movie = ["스파이럴","더 스파이","내겐 너무 소중한 너","극장판 귀멸의 칼날","비와 당신의 이야기","크루즈 패밀리","노매드랜드","아들의 이름으로","미나리","아이들은 즐겁다"]
plt.xticks(x,movie,rotation='vertical')
y=[7.93,8.52,9.90,9.30,6.73,9.21,8.42,8.28,7.70,9.43]
plt.bar(x,y)
plt.suptitle('movie review grade')
plt.xlabel('영화')
plt.ylabel('평점')
plt.legend()
plt.show()