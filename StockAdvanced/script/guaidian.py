# -*- coding: utf-8 -*-
import urllib
import json
from quantdata.db.mongo import Mongo
from quantdata.stock import quotes

def check_stock(code):
    mongo = Mongo()
    db = mongo.getDB()
    cursor = db.mainreports.find({"code":code})
    report_list = dict()
    for row in cursor:
        report_list[str(row['date'])] = row
    if len(report_list) == 0:
        return False,None,None
    key_list = list(report_list.keys())
    key_list.sort()
    key_list.reverse()
    last_two_quarter = key_list[0:2]
    last_date = str(key_list[0])
    year = int(last_date[0:4])
    last_three_year = [str(year-1)+"-12-31",str(year-2)+"-12-31",str(year-3)+"-12-31"]
    last_three_year2 = [v for v in last_three_year if v in key_list]
    "连续三年业绩增长都小于30%，最近3个季度业绩增长大于30%"
    year_grow = []
    for key in last_three_year2:
        if report_list[key]['profits_yoy']:
            year_grow.append(report_list[key]['profits_yoy'])
    quarter_grow = []
    for key in last_two_quarter:
        if report_list[key]['profits_yoy']:
            quarter_grow.append(report_list[key]['profits_yoy'])

    if (sum(year_grow)/3)!=0 and (max(quarter_grow) - sum(year_grow)/3)/abs((sum(year_grow)/3)) > 1:
        return True,quarter_grow,year_grow
    return False,quarter_grow,year_grow
        
if __name__ == "__main__":
    
    
    
    stokList = quotes.get_stock_hq_list()
    data_list = []
    for i in stokList.index:
        try:
            flag, quarter_grow,year_grow = check_stock(stokList.loc[i,"code"])
            if flag:
                data = {"code":stokList.loc[i,"code"],"quarter_grow1":quarter_grow[0],"quarter_grow2":quarter_grow[1],\
                        "year_grow1":year_grow[0],"year_grow2":year_grow[1],"year_grow3":year_grow[2],"mktcap":stokList.loc[i,"mktcap"],\
                        "name":stokList.loc[i,"name"]}
                data_list.append(data)
        except:
            continue
    mongo = Mongo()
    db = mongo.getDB()
    db["guaidian_list"].remove()
    db["guaidian_list"].insert(data_list)