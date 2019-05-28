#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:41:35 2019

@author: yura
"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import random

songName=[]
songId=[]
albumName=[]
duration=[]
playCount=[]

df=pd.read_excel('五月天专辑信息.xlsx')
albumString=df['专辑字符']


headers={
             'Connection': 'keep-alive',
             'Cookie':'',
             'User-Agent': ''
             }

url='https://www.xiami.com/album/{}'

for albumId in albumString[13:]:
    print('正在爬取{}'.format(albumId))
    full_url=url.format(albumId)
    res = requests.get(full_url, headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    
    #歌曲名字,专辑名字
    sn=soup.select('.song-name')
    for i in range(len(sn)):
        songName.append(sn[i].text)
        albumName.append(soup.select('.album-name')[0].text)
    #歌曲id
    for item in sn:
        a=item.find_all('a')
        for m in a:
            songId.append(m.get('href')[6:])
    #时长
    d=soup.select('.duration')
    for i in range(len(d)):
        duration.append(d[i].text)
    pc=soup.select('.playCount-container')
    for p in range(len(pc)):
        playCount.append(pc[p].text)
    
    time.sleep(random.random()*3+1)

print('爬取成功啦！')
result={'专辑名字':albumName,'歌曲名字':songName,'歌曲ID':songId,'歌曲时长':duration,'播放量':playCount}
results=pd.DataFrame(result)
results.info()
results.to_excel('五月天歌曲清单.xlsx')


