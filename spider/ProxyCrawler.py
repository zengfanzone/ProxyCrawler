# coding:utf-8
import os
from configparser import ConfigParser
from bs4 import BeautifulSoup
from spider import ChecKProxy
from spider import GetProxy
#1、从网上抓取代理IP地址
#2、校验代理IP是否有效，进行筛选
class ProxyCrawler(object):
    def __init__(self):
        pass
    def GetValidProxyPool(self):
        ProxyPool = set()
        ValidProxyPool = set()

        ProxyPool = GetProxy.GetXiCiProxy().getProxy()
        if not ProxyPool:
            print("Sorry, proxy not found!")
        ValidProxyPool = ChecKProxy.CheckProxyByFeature().CheckProxyPool(ProxyPool)
        if not ValidProxyPool:
            print("Sorry, valid proxy not found!")
        return ValidProxyPool
spider = ProxyCrawler()
spider.GetValidProxyPool()




