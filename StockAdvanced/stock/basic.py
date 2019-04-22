# -*- coding:utf-8 -*-
import json
import pandas as pd
import numpy as np
from quantdata import cons as ct

from urllib.request import urlopen, Request


def get_main_report(code):
    """
        获取主要指标数据
    Parameters
    --------
    code:str 股票代码 e.g:600000
       
    Return
    --------
    DataFrame
        eps, 基本每股收益（元）
        net_profits,净利润（万元）
        profits_yoy, 净利润同比增长率（%）
        non_recurring_profits,扣非净利润（万元）
        business_income,营业总收入（万元）
        business_income_yoy, 营业总收入同比增长率（%）
        bvps,每股净资产（元）
        roe, 净资产收益率（%）
        diluted_roe,净资产收益率-摊薄（%）
        debet_ratio,资产负债比率（%）
        reserved_per_share,每股资本公积金（元）
        retained_eps,每股未分配利润（元）
        cashflow_per_share,每股经营现金流（元）
        gross_profit_rate,销售毛利率（%）
        inventory_turnover,存货周转率（%）
    """
    data = _get_main_report(code)
    #if data is not None and not data.empty:
        #data = data.drop_duplicates('code')
        #data['code'] = data['code'].map(lambda x:str(x).zfill(6))
    return data

def _convert_to_float(str_):
    try:
        return float(str_)
    except ValueError:
        return np.NaN

def _get_main_report(code):
    df = pd.DataFrame(columns = ct.MAIN_DATA_COL)
    try:
        request = Request(ct.THS_MAIN_DATA_URL%(code))
        request.add_header("User-Agent", ct.USER_AGENT)
        text = urlopen(request, timeout=ct.API_TIMEOUT).read()
        text = text.decode('gbk') if ct.PY3 else text 
        js = json.loads(text.strip())
        if js is None:
            return df
        i = 0
        for col in df.columns:
            if i >= len(js['report']):
                break
            if i > 0:
                df[col] = list(map(_convert_to_float,js['report'][i]))
            else:
                df[col] = js['report'][i]
            i+=1
        return df
    except Exception as e:
        print(e) 
        
if __name__ == '__main__':
    
    df = get_main_report('600000')
    #print(df)
    d = "2013-12-31"
    
    print(df[df.date>d])
    