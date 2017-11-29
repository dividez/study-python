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
    def __init__(self, baseUrl, seeLZ, floorTag):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.baseURL = baseUrl
        self.tool = Tool()
        self.floor = 1
        self.file = None
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.defaultTitle = u"百度贴吧"
        # 是否写入楼分隔符的标记
        self.floorTag = floorTag

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

    def getTitle(self, page):
        pattern = re.compile('<h3.*?core_title_txt pull-left text-overflow.*?>(.*?)</h3>', re.S)
        title = re.search(pattern, page)
        return title.group(1).strip()

    def getPageNumber(self, page):
        pattern = re.compile('<li.*?l_reply_num.*?<span.*?class="red">(.*?)</span>', re.S)
        pageNumber = re.search(pattern, page)
        return pageNumber.group(1).strip()

    def getContent(self, page):
        pattern = re.compile('<div.*?id="post_content.*?class="d_post_content j_d_post_content.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorLine = "\n" + str(
                    self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNumber(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1, int(pageNum) + 1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        # 出现写入异常
        except IOError, e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"


if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseURL, 1, '1')
    bdtb.start()
