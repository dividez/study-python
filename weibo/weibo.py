# -*- coding: utf-8 -*-
import codecs
import csv
import re

import jieba
import jieba.analyse
from matplotlib.image import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt

__author__ = 'Jim'

import requests


class WBWordCloud:
    def __init__(self, cookies, MaxPageNumber):
        self.cookies_are = cookies
        self.MaxPageNumber = MaxPageNumber

    def wb(self):
        api = "https://m.weibo.cn/index/my?format=cards&page=%s"
        cookies = dict(
            cookies_are=self.cookies_are)
        for i in range(1, int(self.MaxPageNumber)):
            print u'正在抓取微博第%d页数据....' % i
            response = requests.get(url=api % i, params={}, cookies=cookies)
            data = response.json()[0]
            groups = data.get('card_group') or []
            for group in groups:
                text = group.get('mblog').get('text')
                text = text.encode('utf-8')
                text = self.filter_tags(text).strip()
                text = self.clearning(text)
                yield text

    def clearning(self, text):
        exclude_one = 'Repost'
        exclude_two = '转发微博'
        result_one = text.find(exclude_one)
        result_two = text.find(exclude_two)
        if result_one == 0 or result_two == 0:
            return ''
        return text

    def filter_tags(self, htmlstr):
        # 先过滤CDATA
        re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
        re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
        re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
        re_br = re.compile('<br\s*?/?>')  # 处理换行
        re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        re_comment = re.compile('<!--[^>]*-->')  # HTML注释
        re_kuo = re.compile('//@')
        re_o = re.compile('\[|\]')
        s = re_cdata.sub('', htmlstr)  # 去掉CDATA
        s = re_script.sub('', s)  # 去掉SCRIPT
        s = re_style.sub('', s)  # 去掉style
        s = re_br.sub('\n', s)  # 将br转换为换行
        s = re_h.sub('', s)  # 去掉HTML 标签
        s = re_comment.sub('', s)  # 去掉HTML注释
        s = re_kuo.sub('', s)
        s = re_o.sub('', s)
        # 去掉多余的空行
        blank_line = re.compile('\n+')
        s = blank_line.sub('\n', s)
        return s

    def write_csv(self, texts):
        with codecs.open('./weibo.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=["text"])
            writer.writeheader()
            for text in texts:
                writer.writerow({"text": text})

    def read_csv(self):
        with codecs.open('./weibo.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row['text']

    def word_segment(self, texts):
        jieba.analyse.set_stop_words("./stop_words.txt")
        for text in texts:
            tags = jieba.analyse.extract_tags(text, topK=20)
            return " ".join(tags)

    def generate_img(self, texts):
        data = " ".join(text for text in texts)
        mask_img = imread('heart-mask.jpg', format=True)
        wordcloud = WordCloud(
            font_path='msyh.ttc',
            background_color='white',
            mask=mask_img
        ).generate(data)
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.savefig('./heart.jpg', dpi=600)

    def start(self):
        print u'正在抓取微博数据....'
        self.write_csv(self.wb())
        self.word_segment(self.read_csv())
        print u'微博数据抓取完毕，正在制作词云....'
        self.generate_img(self.read_csv())
        print u'制作词云完毕....'


if __name__ == '__main__':
    cookie = '_T_WM=05cad175256e0ebe6bd9bfc6cb7c83a5; ALF=1514525058; SCF=AovAf3iaf5_5A-7191mBIHAdrnGPBDSZ3d_2017U8-Ylgo9U-V0K9S4h182ldHCZLew-otZrWI01T7rR9vHXKy8.; SUB=_2A253Gy7GDeRhGeNK6lsQ8yrEzTiIHXVU57KOrDV6PUJbktAKLXn9kW1NSVPD_x8NYEAQ_pDt6-luZ6k3UGdC4I1c; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5ugm.Doobl8_njRi2vp82X5JpX5K-hUgL.Fo-XeK.pe0BRSoB2dJLoI7DSqg_LxrHXUPiL; SUHB=0idrYDOg90J9ug; SSOLoginState=1512005271'
    wb = WBWordCloud(
        cookie,
        100)

    wb.start()
