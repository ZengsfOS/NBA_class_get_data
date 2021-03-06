#!/sur/bin/env python
# -*- coding:utf-8 -*-
# author:zengsf
# time:2018/10/22

import requests
from nba.headers import header


def get_Data(url):
    '''获取html文本'''
    try:
        headers = {'User-Agent': header()}
        response = requests.get(url, headers)
        # print(response)
        # print(response.encoding)
        if response.status_code == 200:
            return response.text.encode("ISO-8859-1").decode("utf-8")
        return None
    except:
        return None
