#!/sur/bin/env python
# -*- coding:utf-8 -*-
# author:zengsf
# time:2018/10/25

import requests
from bs4 import BeautifulSoup
import random


def get_ip_lists(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,"lxml")
    ips = soup.find_all("tr")
    # print(ips)
    ip_lists = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all("td")
        # print(tds)
        ip_lists.append(tds[5].text + "://" + tds[1].text)
    return ip_lists


def get_random_ip(ip_lists):
    proxie_ip = random.choice(ip_lists)
    proxies = {'http':proxie_ip}
    return proxies


#if __name__ == "__main__":
def run():
    url = "http://www.xicidaili.com/nn/"
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
    ip_lists = get_ip_lists(url, headers)
    proxies = get_random_ip(ip_lists)
    # print(proxies)
