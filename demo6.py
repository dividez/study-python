# -*- coding: utf-8 -*-
import re

__author__ = 'Jim'

import requests


def wb():
    api = "https://m.weibo.cn/index/my?format=cards&page=%s"
    cookies = dict(
        cookies_are="_T_WM=05cad175256e0ebe6bd9bfc6cb7c83a5; ALF=1512876008; SCF=AovAf3iaf5_5A-7191mBIHAdrnGPBDSZ3d_2017U8-YlirSDO7lRKzbiE5rUJqENlVBodEni9I_SW1HAQeRQo9E.; SUB=_2A253ATKuDeRhGeNK6lsQ8yrEzTiIHXVUCl7mrDV6PUJbktAKLWTekW0rrGadQ37Paw83FgGOwpYzKoERwA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5ugm.Doobl8_njRi2vp82X5JpX5K-hUgL.Fo-XeK.pe0BRSoB2dJLoI7DSqg_LxrHXUPiL; SUHB=02MvDN_l_KZ-Ht; SSOLoginState=1510294270")
    for i in range(1, 30):
        response = requests.get(url=api % i, params={}, cookies=cookies)
        data = response.json()[0]
        groups = data.get('card_group') or []
        for group in groups:
            text = group.get('mblog').get('text')
            text = text.encode('utf-8')
            text = filter_tags(text).strip()
            text = clearning(text)
            print text
            # yield text


def clearning(text):
    exclude_one = 'Repost'
    exclude_two = '转发微博'
    result_one = text.find(exclude_one)
    result_two = text.find(exclude_two)
    if result_one == 0 or result_two == 0:
        return ''
    return text


def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    return s


wb()

# print clearning('Repost')
