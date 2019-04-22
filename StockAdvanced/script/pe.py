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
    stock_list = st.MktEqud(tradeDate="20160513",field="ticker,PE,secShortName")
    if not isinstance(stock_list,pd.DataFrame) or stock_list.empty:
        return
    
    stock_list['ticker'] = stock_list['ticker'].map(lambda x: str(x).zfill(6))
    result = []
    mongo = Mongo()
    db = mongo.getDB()
    for i in stock_list.index:
        code = stock_list.loc[i,'ticker']
        pe =  stock_list.loc[i,'PE']
        name =  stock_list.loc[i,'secShortName']
        if np.isnan(pe):
            continue
        cursor = db.year_min_value.find({"ticker":code})
        if cursor.count() <= 0:
            continue
        pe_list = []
        for row in cursor:
            pe_list.append(row['pe'])
        min_pe = min(pe_list)
        rate = (pe - min_pe)/min_pe
        result.append({"code":code,"name":name,"pe":pe,"min_pe":min_pe,"rate":rate})
    df = pd.DataFrame(result)
    if db.lowest_pe_stock.find().count() > 0:
        db.lowest_pe_stock.remove()
    db.lowest_pe_stock.insert(json.loads(df.to_json(orient='records')))    
    
    
if __name__ == '__main__':
    run()
    
