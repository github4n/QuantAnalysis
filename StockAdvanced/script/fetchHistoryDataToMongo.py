import tushare as ts
import quantdata.cons as ct
from quantdata.db.mongo import Mongo
from datetime import datetime
from quantdata import logger
import time
import json
import pymongo

ts.set_token(ct.DATA_YES_TOKEN)

def run():
    
    '''get qoute data '''
    
    #set log 
    LOGGER_NAME = "HISTORY_DATA"
    mylog = logger.getLogger(LOGGER_NAME)
    
    #get the stock list
    today = datetime.strftime(datetime.today(),"%Y%m%d")
    mongo = Mongo()
    db = mongo.getDB()
    cursor = db.stock_list.find({"listStatusCD":"L"})
    for row in cursor:
        ticker = str(row['ticker'])
        mylog.info("update history data of %s"%(ticker))
        exchangeCD = str(row['exchangeCD'])
        listDate =  str(row['listDate']).replace("-", "").replace("NaN", "")
        if exchangeCD == 'XSHG' and not ticker.startswith("6"):
            continue
        #get hist data
        cursor2 = db.cn_stock_hist.find({"ticker":ticker}).sort("tradeDate",pymongo.DESCENDING).limit(1)
        st = ts.Market()
        if cursor2.count() > 0:
            start_date = str(cursor2[0]['tradeDate']).replace("-", "")
            df = st.MktEqud(ticker=ticker,beginDate=start_date, endDate=today, field="")
            if df is not None and not df.empty:
                if df['accumAdjFactor'][0] == 1:
                    mylog.info("update new  data of %s from %s"%(ticker,start_date))
                    df = df[1:]
                else:
                    mylog.info("factor change remove  data of %s"%(ticker))
                    db.cn_stock_hist.remove({"ticker":ticker})
                    df = st.MktEqud(ticker=ticker,beginDate=listDate, endDate=today, field="")
        else:
            mylog.info("fisrt insert  data of %s"%(ticker))
            df = st.MktEqud(ticker=ticker,beginDate=listDate, endDate=today, field="")
        
        
        if df is not None and not df.empty:
            mylog.info("processing insert of %s"%(ticker))
            df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
            db.cn_stock_hist.insert(json.loads(df.to_json(orient='records')))
        time.sleep(1)
if __name__ == '__main__':
    
    #st = ts.Market()
    #df = st.MktEqud(ticker='002174',beginDate="20160505", endDate="20160505", field="")
    #print df[1:]
    run()
