# -*- coding: utf-8 -*-
import re
import urllib2

__author__ = 'Jim'


class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print u'连接失败,错误原因' + e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        if not page:
            print '页面获取失败。。。。'
            return None
        pattern = re.compile('<h3.*?core_title_txt pull-left text-overflow.*?>(.*?)</h3>', re.S)
        title = re.search(pattern, page)
        print title.group(1).strip()

    def getPageNumber(self):
        page = self.getPage(1)
        if not page:
            print '页面获取失败。。。。'
            return None
        pattern = re.compile('<li.*?l_reply_num.*?<span.*?class="red">(.*?)</span>', re.S)
        pageNumber = re.search(pattern, page)
        print pageNumber.group(1).strip()
        self.getContent(page)

    def getContent(self, page):
        pattern = re.compile('<div.*?id="post_content.*?class="d_post_content j_d_post_content.*?>(.*?)</div>', re.S)
        content = re.findall(pattern, page)
        for con in content:
            print con


if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    # baseURL = 'http://tieba.baidu.com/p/5446246276'
    bdtb = BDTB(baseURL, 1)
    bdtb.getPageNumber()
