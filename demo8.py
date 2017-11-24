# -*- coding: utf-8 -*-
import re
import urllib2

__author__ = 'Jim'

# 参考链接：http://cuiqingcai.com/990.html

class qsbk:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'https://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print u'连接糗事百科失败,错误原因' + e.reason
                return None

    # 传入某一页代码，返回本页的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile('<div.*?clearfix">.*?<h2.*?>(.*?)</h2>.*?<div.*?content">.*?<span.*?>(.*?)</span>.*?' +
                             '<span.*?stats-vote">.*?<i.*?number">(.*?)</i>.*?' +
                             '<span.*?stats-comments">.*?<i.*?number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip()])

        return pageStories

    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input();
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t发布内容:%s\t赞:%s\t评论:%s" % (page, story[0], story[1], story[2], story[3])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            print len(self.stories)
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)


spider = qsbk()
spider.start()
