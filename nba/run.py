#!/sur/bin/env python
# -*- coding:utf-8 -*-
# author:zengsf
# time:2018/10/22
from nba.method import GETDATA
import nba.dataceData


def getDataKing(dataceAllLink):
    datace = GETDATA(dataceAllLink)
    datace_html = datace.gethtml()
    # print(datace_html)
    datace_links = nba.dataceData.getDataceSecondLink(datace_html)
    for datace_link in datace_links:
        print(datace_link)
        name_link = [i for i in datace_link.items()]
        name, link = name_link[0][0], name_link[0][1]
        # if name == "得分王":
        # 将各项数据王中的链接进行解析，获取数据
        datas = nba.dataceData.getDataceData(datace_link)
        print(name)
        # 这里是循环遍历生成器返回的数据
        for data in datas:
            pass
            # print(data)          #TODO  这里在来一个mongodb模块就可以搞定


if __name__ == "__main__":
    # 创建一个对象
    home = GETDATA("http://www.stat-nba.com/")
    # 获取到请求的html
    data = home.gethtml()
    # 获取到首页中16个链接
    links = GETDATA.getTitleLink(data)
    print(links)
    # 获取到各项数据王的链接
    dataceAllLink = GETDATA.getlink(links, "各项数据王")
    # print(dataceAllLink)
    # 将或有的各项数据王的信息都用这个方法来完成
    getDataKing(dataceAllLink)

