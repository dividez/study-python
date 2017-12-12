# -*- coding: utf-8 -*-
import requests as req
from bs4 import BeautifulSoup
from http import cookiejar

__author__ = 'Jim'

headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
}
session = req.session()
session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
# try:
#     print(session.cookies)
#     session.cookies.load(ignore_discard=True)
#
# except:
#     print("还没有cookie信息")


def login_page():
    url = 'https://www.zhihu.com/?next=%2Ftopic#signin'
    requests = session.get(url, timeout=5, headers=headers)
    return requests.text


def get_xsrf_code():
    soup = BeautifulSoup(login_page(), "html.parser")
    xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
    return xsrf


def login():
    session = req.session()
    login_url = 'https://www.zhihu.com/login/phone_num'
    data = {
        'account': '',
        'password': '',
        '_xsrf': get_xsrf_code()}
    response = session.post(login_url, data=data, headers=headers)
    login_code = response.json()
    print(login_code)


if __name__ == '__main__':
    login()
