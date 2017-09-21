# coding:utf-8

import requests
import re
from bs4 import BeautifulSoup

#从http://www.xici.net.co/nn/获取代理地址
class GetXiCiProxy(object):
    def __init__(self):
        self.headers= {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)',
    }

    def getProxy(self):
        ProxyPool = set()
        url = 'http://www.xicidaili.com/nn/'
        r = None
        try:
            r = requests.get(url,headers = self.headers,timeout = 10)
        except Exception as e:
            print("Exception Message:" + str(e))
        if r.status_code != 200:
            return None
        htmlText = r.text
        soup = BeautifulSoup(htmlText,'html.parser')
        ipTable = soup.find('table', attrs={'id':'ip_list'})
        if not ipTable:
            print("Error: Visit http://www.xicidaili.com/nn/ to see detail.")
            return None

        for trTag in ipTable.find_all('tr'):
            lst = list(trTag.find_all('td'))
            if len(lst) != 10:
                continue
            ip = ''.join(lst[1].stripped_strings)
            port = ''.join(lst[2].stripped_strings)
            item = ip + ':' + port
            if re.match(r'^[\d\.:]+$', item):
                ProxyPool.add(item)
        print("Get proxy count: " + str(len(ProxyPool)))
        return ProxyPool





