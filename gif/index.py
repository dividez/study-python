# -*- coding: utf-8 -*-
import random
import time

import os

__author__ = 'Jim'

import requests


class gif:
    def __init__(self, api_url, StartPageNumber, MaxPageNumber):
        self.api_url = api_url
        self.StartPageNumber = StartPageNumber
        self.MaxPageNumber = MaxPageNumber
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def _getPage(self):
        try:
            for i in range(int(self.StartPageNumber), int(self.MaxPageNumber)):
                print u'正在抓取第%d页数据....' % i
                datas = requests.get(url=self.api_url + str(i), timeout=5, headers=self.headers)
                datas = datas.json()
                datas = datas.get('gifs') or datas.get('data_list') or []
                for data in datas:
                    yield data

        except requests.RequestException as e:
            print(e)

    def _saveGif(self):
        dirpath = './gif'
        if not os.path.exists(dirpath):  # 判断是否存在新文件夹，否则创建
            os.mkdir(dirpath)
        data = self._getPage()
        for i in data:
            time_str = str(int(time.time()) * 1000) + str(random.randint(0, 99))
            if not i.has_key('gif_thumb'):
                continue
            if not i.has_key('hitKeyword'):
                continue
            hitKeyword = i['hitKeyword']
            img_url = requests.get(i['gif_thumb'], timeout=15, headers=self.headers)
            img_name = hitKeyword + time_str + '.gif'
            if not os.path.exists(dirpath + '/' + hitKeyword):  # 判断是否存在新文件夹，否则创建
                os.mkdir(dirpath + '/' + hitKeyword)
            print u'正在偷偷的将动图保存为', img_name
            if img_url.status_code == 200:
                open('./gif/' + hitKeyword + '/' + img_name, 'wb').write(img_url.content)

    def start(self):
        self._saveGif()
        print u'抓取完毕开启你的装b之旅吧。。。'


if __name__ == '__main__':
    api_url = 'https://www.dongtu.com:9999/hot/gif?page='
    StartPageNumber = 10
    MaxPageNumber = 20
    gif = gif(api_url, StartPageNumber, MaxPageNumber)
    gif.start()
