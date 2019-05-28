#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 07:25:17 2019

@author: yura
"""

import requests
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd
import re
import random

songName=[]
songIds=[]
favCount=[]
commentCount=[]
lyrics=[]
newSubName=[]


songwriters=[] #作词
composer=[] #作曲
arrangement=[] #编曲
albumId=[]
albumName=[]

hotComment1=[]
commentLike1=[]

playCount=[]

df=pd.read_excel('五月天歌曲清单.xlsx')
albumString=df['歌曲ID']
url='https://www.xiami.com/song/{}'


#cookie需要经常保持更新
for songid in albumString:
    print('正在爬取{}'.format(songid))
    full_url=url.format(songid)
    headers={

                 'Connection': 'keep-alive',
                 'Cookie':'',
                 'User-Agent': ''
                 }
    res = requests.get(full_url, headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
  
    songName.append(soup.select('.song-name')[0].text)   
    songIds.append(songid)
    
    search_data=re.findall('(</span>)(.*?)span class="ripple" style="height',res.text,re.S)   
    favCount.append(str(search_data[1])[-10:-3].replace('n','').replace('>','').replace('n',''))
    
    if(soup.select('.lyric-content')):
        lyrics.append(soup.select('.lyric-content')[0].text)
    else:
        lyrics.append('无')  
        
    if(soup.select('.song-subname')):
        newSubName.append(soup.select('.song-subname')[0].text)
    else:
        newSubName.append('')
    
    creatInfo=soup.select('.info-value')
    albumName.append(creatInfo[0].text)
    songwriters.append(creatInfo[1].text) #作词
    composer.append(creatInfo[2].text) #作曲
    arrangement.append(creatInfo[3].text) #编曲
    
    playCount.append(soup.select('.count')[0].text[1:])
    commentCount.append(soup.select('.count'))
  
    #第一条热门评论
    if(soup.select('.comment-text')):
        hotComment1.append(soup.select('.comment-text')[0].text)
    else:
        hotComment1.append('')
    #第一条热门评论的点赞数（其实数据不太准） 
    if(len(soup.select('.count'))>8):
         commentLike1.append(soup.select('.count')[8].text)
    else:
         commentLike1.append('无')

    time.sleep(random.random()*5)

result={'歌曲名字':songName,'别名':newSubName,'歌曲Id':songIds,'收藏数量':favCount,'播放数量':playCount,'评论数量':commentCount,'作词':songwriters,'作曲':composer,'编曲':arrangement,'专辑名字':albumName,'歌词':lyrics,'热门评论1':hotComment1,'热门评论赞1':commentLike1}
results=pd.DataFrame(result)
results.info()
results.to_excel('五月天歌曲详情1500.xlsx')

