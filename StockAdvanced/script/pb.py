from quantdata.db.mongo import Mongo

from quantdata.stock import quotes
import pandas as pd
import numpy as np
import tushare as ts
import quantdata.cons as ct
import json
from datetime import datetime

def run():
    ts.set_token(ct.DATA_YES_TOKEN)
    st = ts.Market()
    today = datetime.strftime(datetime.today(),"%Y%m%d")
    stock_list = st.MktEqud(tradeDate=today,field="ticker,PB,secShortName")
    if not isinstance(stock_list,pd.DataFrame) or stock_list.empty:
        return
    
    stock_list['ticker'] = stock_list['ticker'].map(lambda x: str(x).zfill(6))
    result = []
    mongo = Mongo()
    db = mongo.getDB()
    for i in stock_list.index:
        code = stock_list.loc[i,'ticker']
        pb =  stock_list.loc[i,'PB']
        name =  stock_list.loc[i,'secShortName']
        if np.isnan(pb):
            continue
        cursor = db.year_min_value.find({"ticker":code})
        if cursor.count() <= 0:
            continue
        pb_list = []
        for row in cursor:
            pb_list.append(row['pb'])
        min_pb = min(pb_list)
        rate = (pb - min_pb)/min_pb
        result.append({"code":code,"name":name,"pb":pb,"min_pb":min_pb,"rate":rate})
    df = pd.DataFrame(result)
    if db.lowest_pb_stock.find().count() > 0:
        db.lowest_pb_stock.remove()
    db.lowest_pb_stock.insert(json.loads(df.to_json(orient='records')))    
    
    
if __name__ == '__main__':
    run()
    
