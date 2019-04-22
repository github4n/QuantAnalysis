# -*- coding: utf-8 -*-
import urllib, urllib2
import json
from quantdata.db.mongo import Mongo
from quantdata.stock import quotes

def get_forcast_list(query_text):
    res = quotes.query_iwencai(query_text)
    
    if res is None or  not res.has_key("result"):
        pass
    
    forcast_list = {}
    for item in res["result"]:
        if type(item[5]) is str and not item[5].isdigit():
            forcast_list[item[0][0:6]] = dict(rate=0,detail=item[10][1],name=item[1],mktcap=item[6])
        else:
            forcast_list[item[0][0:6]] = dict(rate=float(item[5]),detail=item[10][1],name=item[1],mktcap=item[6])
    return forcast_list

def check_stock(code,forcast_rate):
    query_text = '业绩预增,预告业绩变动幅度排序'
    
    mongo = Mongo()
    db = mongo.getDB()
    cursor = db.mainreports.find({"code":code})
    report_list = dict()
    for row in cursor:
        report_list[str(row['date'])] = row
    if len(report_list) == 0:
        return False,None
    key_list = report_list.keys()
    key_list.sort()
    key_list.reverse()
    last_four_quarter = key_list[0:4]
   
    "连续三年业绩增长都小于30%，最近3个季度业绩增长大于30%"
    
    quarter_profit_grow = []
    for key in last_four_quarter:
        if report_list[key]['profits_yoy']:
            quarter_profit_grow.append(report_list[key]['profits_yoy'])


    if (sum(quarter_profit_grow)/4)!=0 and (forcast_rate - sum(quarter_profit_grow)/4)/abs((sum(quarter_profit_grow)/4)) > 1:
        return True,quarter_profit_grow
    return False,quarter_profit_grow

if __name__ == "__main__":
    
    forcast_list = get_forcast_list("业绩预增,预告业绩变动幅度排序,市值")
    data_list = []
    for code,value in forcast_list.items():
        
        if value['rate'] == 0:
            continue
        flag,quarter_grow = check_stock(code,value['rate'])
        if flag:
            data = {"code":code,"quarter_grow":"/".join([str(x) for x in quarter_grow]),"forcat_detail":value['detail']}
            data["name"] = value["name"]
            data["rate"] = value["rate"]
            data["mktcap"] = value["mktcap"]
            
            data_list.append(data)
    
    mongo = Mongo()
    db = mongo.getDB()
    db["forcast_list"].remove()
    db["forcast_list"].insert(data_list)
        