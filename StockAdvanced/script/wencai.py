# -*- coding: utf-8 -*-
import urllib, urllib2
import json
from quantdata.db.mongo import Mongo


URL_IWENCAI_QUERY = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&perpage=4000&f=1&qs=1&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=%s"
#URL_IWENCAI_QUERY_EXPORT = "http://www.iwencai.com/stockpick/export?token=%s"
# query iwencai and get a full stock symbol list
def query_iwencai(query):
    url = URL_IWENCAI_QUERY % (urllib.quote(query))
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.3',
        'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
        'Referer': 'http://www.iwencai.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko',
        'X-Requested-With': 'XMLHttpRequest',
    }
    #print(url)
    try:
        data = None
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        compressedData = response.read()
        # look for: "token":"3c056e348add1a00a81b17e2ec4280b4"
        #print compressedData
        lines = compressedData.split('\n')
        for line in lines:
            if line.find("allResult") > 0:
                #print line
                # eat up final characters that is not '}'
                result = line[16:-1]
                while result[-1] != '}':
                    result = result[:-1]
                return json.loads(result)
        
    except:
        pass
    
    return None

def query_store(query,store):
    res = query_iwencai(query)
    if res is None or  not res.has_key("result"):
        pass
    ticker_list = []
    for item in res["result"]:
        ticker_list.append(dict(ticker=item[0][0:6]))
    mongo = Mongo()
    db = mongo.getDB()
    db[store].remove()
    db[store].insert(ticker_list)
    

if __name__ == "__main__":
    
    growstock = "流通市值小于200亿;连续3年 年度净利润增长率小于30%;连续3个季度 净利润单季度增长率大于30%;"
    query_store(growstock,"guaidian_list")
