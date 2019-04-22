# -*- coding:utf-8 -*-

import sys
PY3 = (sys.version_info[0] >= 3)

'''爬虫设置'''
API_TIMEOUT = 50
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"




'''同花顺基本面数据'''
THS_MAIN_DATA_URL = 'http://basic.10jqka.com.cn/%s/flash/main.txt'

''' 
[日期,基本每股收益,净利润,净利润同比增长率,扣非净利润,营业总收入,营业总收入同比增长率,
    每股净资产,净资产收益率,净资产收益率-摊薄,资产负债比率,每股资本公积金,
    每股未分配利润,每股经营现金流,销售毛利率,存货周转率]
'''
MAIN_DATA_COL = ['date','eps', 'net_profits','profits_yoy', 'non_recurring_profits', 'business_income',
               'business_income_yoy',  'bvps', 'roe', 'diluted_roe','debet_ratio','reserved_per_share',
               'retained_eps','cashflow_per_share','gross_profit_rate','inventory_turnover']

THS_DEBT_DATA_URL = 'http://basic.10jqka.com.cn/%s/flash/debt.txt'

THS_BENEFIT_DATA_URL = 'http://basic.10jqka.com.cn/%s/flash/benefit.txt'

THS_CASH_DATA_URL = 'http://basic.10jqka.com.cn/%s/flash/cash.txt'

'''行情接口'''
#param:"[%22hq%22,%22hs_a%22,%22{sort}%22,{asc},{page},{num}]"
SINA_OPEN_API_URL = "http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[%s]"
OPEN_API_PAGE_NUM = 100


#mongo
MONGO_DATABASE = 'stock'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017

#mysql
MYSQL_DATABASE = 'stock'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'Abc1234!'

#datayes
DATA_YES_TOKEN = '68ca84406ff669a2c7e8dfbfb0495460a6befd9d7d39a2336fd11bfa4693d62c'
