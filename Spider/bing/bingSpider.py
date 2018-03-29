# -*- coding: utf-8 -*-
__author__ = 'Jim'

import requests
import re
import time

local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
reg = r"(/az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
read = requests.get(url + a)
f = open('./img/%s.jpg' % local, 'wb')
f.write(read.content)
f.close()
