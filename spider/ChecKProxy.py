import requests

class CheckProxyByFeature(object):
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)',
        }
        self.targeturl = 'http://www.dangdang.com'
        self.feature = '当当'

    def CheckProxyPool(self, ProxyPool):
        ValidProxyPool = set()
        for proxy in ProxyPool:
            flag = self.CheckOneProxy(proxy)
            if flag:
                ValidProxyPool.add(proxy)
        print("Valid Proxy Count: " + str(len(ValidProxyPool)))
        return ValidProxyPool

    def CheckOneProxy(self, proxy):

        proxies = {
            'http': proxy,
            'https': proxy
        }
        r = None
        try:
            r = requests.get(self.targeturl, headers = self.headers, timeout = 10, proxies = proxies)
        except Exception as e:
            print("Error:" + str(e))
            return False
        if r.status_code != 200:
            return False
        if r.text.find(self.feature) < 0:
            return False
        print("Find Proxy:" + str(proxy))
        return True




