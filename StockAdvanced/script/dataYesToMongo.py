import tushare as ts
import quantdata.cons as ct
from quantdata.db.mongo import Mongo
from datetime import datetime
from quantdata import logger
import time
import json

ts.set_token(ct.DATA_YES_TOKEN)


def fetch_stock_list_to_mongo():
    eq = ts.Equity()
    df = eq.Equ(equTypeCD='A', listStatusCD='L', field='')
    df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
    mongo = Mongo()
    db = mongo.getDB()
    cursor = db.stock_list.find()
    if cursor.count() == 0:
        db.stock_list.insert(json.loads(df.to_json(orient='records')))
        
      
def fetch_cnstock_hist_to_mongo():
    
    '''get qoute data '''
    
    #set log 
    LOGGER_NAME = "TONGLIAN_DATA"
    mylog = logger.getLogger(LOGGER_NAME)
    
    #get the stock list
    today = datetime.strftime(datetime.today(),"%Y%m%d")
    mongo = Mongo()
    db = mongo.getDB()
    cursor = db.stock_list.find({"exchangeCD":{"$in":["XSHE","XSHG"]},"listStatusCD":"L"})
    for row in cursor:
        ticker = str(row['ticker'])
        mylog.info("update history data of %s"%(ticker))
        exchangeCD = str(row['exchangeCD'])
        listDate =  str(row['listDate']).replace("-", "").replace("NaN", "")
        if exchangeCD == 'XSHG' and not ticker.startswith("6"):
            continue
        #get hist data
        cursor2 = db.cn_stock_hist.find({"ticker":ticker})
        if cursor2.count() > 0:
            continue
        mylog.info("insert data of %s"%(ticker))
        st = ts.Market()
        df = st.MktEqud(ticker=ticker,beginDate=listDate, endDate=today, field="")
        df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
        db.cn_stock_hist.insert(json.loads(df.to_json(orient='records')))
        time.sleep(1)
    
    #insert to the mongo
def fetch_main_report_to_mongo():
    pass


if __name__ == '__main__':
    
    fetch_stock_list_to_mongo()
    
    fetch_cnstock_hist_to_mongo()
