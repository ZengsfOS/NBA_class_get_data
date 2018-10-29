#!/sur/bin/env python
# -*- coding:utf-8 -*-
# author:zengsf
# time:2018/10/22
import requests
from lxml import etree


class GETDATA(object):
    # 初始化对象
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    # 获取请求url的html
    def gethtml(self):
        self.response = requests.get(self.url, self.headers)
        self.resule = self.response.text.encode("ISO-8859-1").decode("utf-8")
        # print(resule)
        return self.resule

    # 获取首页中分类荣誉中的所有url，以列表的形式返回
    def getTitleLink(html):
        lxml_data = etree.HTML(html)
        html_link_list = lxml_data.xpath('//div[@class="tile-group four"]/div/a')
        link_list = []
        for links in html_link_list:
            link_dict = {}
            link = "http://www.stat-nba.com" + links.xpath('./@href')[0]
            name = links.xpath("./span/text()")[0]
            link_dict[name] = link
            link_list.append(link_dict)
        return link_list

    # 获取到相对应的链接
    def getlink(lists, name):
        for d in lists:
            for i in d:
                if i == name:
                    return d[i]



