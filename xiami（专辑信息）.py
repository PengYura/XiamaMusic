#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:20:02 2019

@author: yura
"""


import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime
import pandas as pd

albumCategory=[]
albumId=[]
albumLogo=[]
albumName=[]
artistName=[]
collects=[]
language=[]
playCount=[]
recommends=[]
songCount=[]
albumStringId=[]
albumStatus=[]
gmtPublish=[]
grade=[]
gradeCount=[]



url='https://www.xiami.com/api/album/getArtistAlbums?_q=%7B%22pagingVO%22:%7B%22page%22:1,%22pageSize%22:60%7D,%22artistId%22:3110,%22category%22:0%7D&_s=dd6d0ef72dda69944fc2fbaa33c5bc6c'

headers={
             'Connection': 'keep-alive',
             'Cookie':'',
             'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
             }
res = requests.get(url, headers=headers)
content=json.loads(res.text,encoding='utf-8')



for album in content['result']['data']['albums']:
    albumCategory.append(album['albumCategory'])
    albumId.append(album['albumId'])
    albumLogo.append(album['albumLogo'])
    albumName.append(album['albumName'])
    artistName.append(album['artistName'])
    collects.append(album['collects'])
    language.append(album['language'])
    playCount.append(album['playCount'])
    recommends.append(album['recommends'])
    songCount.append(album['songCount'])
    albumStringId.append(album['albumStringId'])
    albumStatus.append(album['albumStatus'])
    gmtPublish.append(datetime.datetime.fromtimestamp(int(album['gmtPublish']/1000)))
    grade.append(album['grade'])
    gradeCount.append(album['gradeCount'])

result={'专辑种类':albumCategory,'专辑id':albumId,'专辑封面':albumLogo,'专辑名字':albumName,'艺术家':artistName,'收藏':collects,'语言':language,'播放数':playCount,'推荐':recommends,'歌曲数量':songCount,'专辑字符':albumStringId,'状态':albumStatus,'评分':grade,'评分人数':gradeCount,'发布时间':gmtPublish}
results=pd.DataFrame(result)
results.info()
results.to_excel('五月天专辑信息.xlsx')

