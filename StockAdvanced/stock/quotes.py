# -*- coding:utf-8 -*-

import pandas as pd
import json
from urllib import parse
from quantdata import cons as ct
from urllib.request import urlopen, Request


def get_stock_hq_list():
    """
        获取沪深上市公司列表和行情
    Return
    --------
    DataFrame    
            guba,股吧地址
            symbol,股票代号
            code,股票代码
            name,股票名称
            trade,最新价
            pricechange,涨跌额
            changepercent,涨跌幅
            buy,买入
            sell,卖出
            settlement,昨收
            open,今开
            high,最高
            low,最低
            volume,成交量（手）
            amount,成交额（万）
            ticktime,
            per,市盈率
            per_d,动态市盈率
            nta,每股净资产
            pb,市净率
            mktcap,总市值
            nmc,流通市值
            turnoverratio,换手率(%)
            favor,
            guba,
               
    """
    df =  _get_stock_hq_list(1, pd.DataFrame())
    if df is not None and not df.empty:
        df = df.drop_duplicates('code')
        df['code'] = df['code'].map(lambda x:str(x).zfill(6))
    return df
def _get_stock_hq_list(pageNo, dataArr):

    try:
        #param:["hq","hs_a","{sort}",{asc},{page},{num}]
        hq_list_param = '["hq","hs_a","",0,%d,%d]'%(pageNo,ct.OPEN_API_PAGE_NUM)
        request = Request(ct.SINA_OPEN_API_URL%(parse.quote(hq_list_param,',[]')))
        request.add_header("User-Agent", ct.USER_AGENT)
        text = urlopen(request, timeout=ct.API_TIMEOUT).read()
        text = text.decode('gbk') if ct.PY3 else text 
        js = json.loads(text.strip())
        if js is None:
            return dataArr
        df = pd.DataFrame(js[0]['items'], columns=js[0]['fields'])
        dataArr = dataArr.append(df, ignore_index=True)
        if int(js[0]['count']) > pageNo * ct.OPEN_API_PAGE_NUM :
            pageNo = pageNo+1
            return _get_stock_hq_list(pageNo, dataArr)
        else:
            return dataArr
    except Exception as e:
        print(e)    
if __name__ == '__main__':
    df = get_stock_hq_list()
    print(df)