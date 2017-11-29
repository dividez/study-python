# -*- coding: utf-8 -*-
import re
import urllib2

__author__ = 'Jim'
"""
Description:
    A simple web spider for Crawl Baidu Post Bar posts.
    Reference: http://cuiqingcai.com/993.html    Python爬虫实战二之爬取百度贴吧帖子
Author:     zpy0930@gmail.com
Created Date:   2017年11月29日
Version:        1.0
"""


# 处理页面标签类
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.baseURL = baseUrl
        self.tool = Tool()
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
        floor = 1
        for con in content:
            print floor, u"楼------------------------------------------------------------------------------------------------------------------------------------\n"
            print self.tool.replace(con)
            floor += 1


if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseURL, 1)
    bdtb.getPageNumber()
