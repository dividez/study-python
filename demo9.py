# -*- coding: utf-8 -*-
import hashlib
import urllib
import urllib2

__author__ = 'Jim'


class apiTest:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def post(self, url, data={}):
        try:
            request = urllib2.Request(url, headers=self.headers)
            data = urllib.urlencode(data)
            response = urllib2.urlopen(request, data)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print u'连接失败,错误原因' + e.reason
                return None

    def signature(self, param, secret_key, url):
        data = sorted(param)
        sign_string = ''
        for v in data:
            sign_string = sign_string + str(param[v])
        sign_string = sign_string + secret_key
        skey = hashlib.md5(sign_string).hexdigest()
        param['signature'] = skey
        return self.post(url, param)


if __name__ == '__main__':
    secret_key = ''
    group_id = ''
    param = {

    }
    url = ''
    api = apiTest()
    print api.signature(param, secret_key, url)
