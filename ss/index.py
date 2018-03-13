# -*- coding: utf-8 -*-
import codecs
import csv
import json

import requests
import base64
import time
import qrcode

__author__ = 'Jim'


class ss:
    def __init__(self):
        self.api_url = 'https://free-ss.site/ss.php?_=%s'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.list_key = ['count', 'ip', 'port', 'password', 'method', 'time', 'location']

    def getData(self):
        try:
            time_str = str(int(time.time()) * 1000)
            url = self.api_url % time_str
            list_data = []
            datas = requests.get(url, timeout=5, headers=self.headers)
            datas = datas.json()
            datas = datas.get('data') or []
            for data in datas:
                other_data = self._create(data)
                new_data = data + other_data
                list_data.append(new_data)

            print('数据抓取完毕，开始写入文件..')
            self._write_csv(list_data)

        except requests.RequestException as e:
            print(e)

    def _create(self, data):
        ss_str = data[4] + ':' + data[3] + '@' + data[1] + ':' + data[2]
        base64_str = base64.b64encode(str.encode(ss_str))
        ss_base64_str = 'ss://' + bytes.decode(base64_str)
        return [
            ss_str,
            bytes.decode(base64_str),
            ss_base64_str
        ]

    def _write_csv(self, texts):
        with codecs.open('./ss_info.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=["text"])
            writer.writeheader()
            for text in texts:
                writer.writerow({"text": text})

    def _read_csv(self):
        with codecs.open('./ss_info.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row['text']


if __name__ == '__main__':
    ss = ss()

