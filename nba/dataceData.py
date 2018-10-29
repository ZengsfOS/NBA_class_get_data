#!/sur/bin/env python
# -*- coding:utf-8 -*-
# author:zengsf
# time:2018/10/24
from lxml import etree
from bs4 import BeautifulSoup
from nba.method import GETDATA


# 获取各项数据王中的二级链接
def getDataceSecondLink(html):
    result = etree.HTML(html)
    datace_links = result.xpath('//*[@id="background"]/div[4]/div[4]/a')
    for datace_link in datace_links:
        dict_link = {}
        name = datace_link.xpath("./div/text()")[0]
        link = "http://www.stat-nba.com" + datace_link.xpath("./@href")[0]
        dict_link[name] = link
        yield dict_link


# 由于各项数据王中的数据都是一样，因此都用这种方法来提取数据
def getDataceData(dict_link):
    # 把传进来的链接字典里面的名字和链接取出来
    name_link = [i for i in dict_link.items()]
    name, link = name_link[0][0], name_link[0][1]
    # 创建GETDATA对象
    html_obj = GETDATA(link)
    # 获取html文本
    html = html_obj.gethtml()
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, "lxml")
    # 获取到soup中里面的第一个tbody里面的说有数据
    tables = soup.find_all("tbody")[0]
    # tables = soup.find_all(attrs={"class" : "stat_box"})[1]
    table_name = ['赛季', '球员', '联盟', '出场', '首发', '时间', '投篮', '命中', '出手', '三分',
             '三分命中', '三分出手', '罚球', '罚球命中', '罚球出手',
             '篮板', '前场', '后场', '助攻', '抢断', '盖帽',
             '失误', '犯规', '得分']
    # lists = list()
    # 遍历tbody里面所有的tr
    for tr in tables.find_all(name="tr"):
        dic = dict()
        l = []
        # 遍历tr里面所有的td且把里面的数据全都取出来，放到列表里面
        for td in tr.find_all(name="td"):
            data = td.string
            l.append(data)
        for index in range(len(l)):
            dic[table_name[index]] = l[index]
            # lists.append(dic)
        # 利用生成器把数据返回回去
        yield dic
    #return list








