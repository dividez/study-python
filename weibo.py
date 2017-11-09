# -*- coding: utf-8 -*-
import codecs
import csv
import json

import jieba
import requests
import demjson
from matplotlib.image import imread
from wordcloud import WordCloud

__author__ = 'Jim'


def signature(params):

    return sortedDictValues2(params)

def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys]

def slist():
    data = {
        'ddd': "asd",
        'aaa':'aasd',
        'ca':'ccccc'
    }
    print signature(data)

slist()
