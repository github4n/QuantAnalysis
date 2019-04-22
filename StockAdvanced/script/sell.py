# -*- coding: utf-8 -*-
import urllib, urllib2
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
    key_list = report_list.keys()
    key_list.sort()
    key_list.reverse()
    last_two_quarter = key_list[0:2]
    last_date = str(key_list[0])
    year = int(last_date[0:4])
    last_three_year = [str(year-1)+"-12-31",str(year-2)+"-12-31",str(year-3)+"-12-31"]
    last_three_year2 = [v for v in last_three_year if v in key_list]
    "连续三年业绩增长都小于30%，最近3个季度业绩增长大于30%"
    year_profit_grow = []
    year_sell_grow = []
    year_gross_profit_rate = []
    for key in last_three_year2:
        if report_list[key]['profits_yoy']:
            year_profit_grow.append(report_list[key]['profits_yoy'])
        if report_list[key]['business_income_yoy']:
            year_sell_grow.append(report_list[key]['business_income_yoy'])
        if report_list[key]['gross_profit_rate']:
            year_gross_profit_rate.append(report_list[key]['gross_profit_rate'])
    quarter_profit_grow = []
    quarter_sell_grow = []
    for key in last_two_quarter:
        if report_list[key]['profits_yoy']:
            quarter_profit_grow.append(report_list[key]['profits_yoy'])
        if report_list[key]['business_income_yoy']:
            quarter_sell_grow.append(report_list[key]['business_income_yoy'])

    if (sum(year_sell_grow)/3)!=0 and (max(quarter_sell_grow) - sum(year_sell_grow)/3)/abs((sum(year_sell_grow)/3)) > 1 \
        and sum(year_profit_grow)/3 < 25 and sum(year_gross_profit_rate)/3 > 20:
        return True,quarter_sell_grow,year_sell_grow,quarter_profit_grow,year_gross_profit_rate
    return False,quarter_sell_grow,year_sell_grow,quarter_profit_grow,year_gross_profit_rate
        
if __name__ == "__main__":
    
    
    
    stokList = quotes.get_stock_hq_list()
    data_list = []
    for i in stokList.index:
        #去掉200亿市值以上的
        try:
            if stokList.loc[i,"mktcap"] > 2000000:
                continue
            flag, quarter_sell_grow,year_sell_grow,quarter_profit_grow,year_gross_profit_rate = check_stock(stokList.loc[i,"code"])
            if flag:
                data = {"code":stokList.loc[i,"code"],"quarter_grow1":quarter_sell_grow[0],"quarter_grow2":quarter_sell_grow[1],\
                        "year_sell_grow":"/".join([str(x) for x in year_sell_grow]),"mktcap":stokList.loc[i,"mktcap"],\
                        "name":stokList.loc[i,"name"],"quarter_profit":"/".join([str(x) for x in quarter_profit_grow]),"year_gross_profit_rate":"/".join([str(x) for x in year_gross_profit_rate])}
                data_list.append(data)
        except:
            continue
    mongo = Mongo()
    db = mongo.getDB()
    db["sell_list"].remove()
    db["sell_list"].insert(data_list)