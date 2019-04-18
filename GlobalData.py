import tushare
import pandas
import time

def Init():
    global _GlobalDict
    _GlobalDict = {}
    #添加金融数据接口
    tushare.set_token('c52ded38c6bb7149aab6f728d131a85fdbfa7538b830cadf763053aa')
    #添加tushare
    _GlobalDict["Tushare"] = tushare
    #添加tusharePro接口
    _GlobalDict["TusharePro"] = tushare.pro_api()
    #添加股票基础数据, 先从本地读取
    StockBasic = pandas.read_csv("Data/StockBasic.csv")
    #StockBasic = _GlobalDict["TusharePro"].stock_basic(exchange='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
    #获取今日股票全部数据, 先从本地读取
    DailyBasic = pandas.read_csv("Data/DailyBasic.csv")
    #DailyBasic = _GlobalDict["TusharePro"].daily_basic(ts_code='', trade_date='20190415', fields='ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,total_share,float_share,free_share,total_mv,circ_mv')
    #合并日数据和股票基础数据
    StockMergeTable = pandas.merge(StockBasic, DailyBasic, on = ['ts_code'], how='inner')
    #去掉Unnamed列
    _GlobalDict["TotalStock"] = StockMergeTable.loc[:, ~StockMergeTable.columns.str.match('Unnamed')]

    #添加普通数据接口
    #按钮是否被选中时颜色
    _GlobalDict["ButtonUnSelectStyle"] = "QPushButton{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QPushButton:hover{background-color: rgb(150, 30, 0);color: rgb(255, 255, 0);}QPushButton:pressed{background-color: rgb(60, 60, 60);color: rgb(0, 0, 255);}"
    _GlobalDict["ButtonSelectStyle"] = "QPushButton{background-color: rgb(200, 69, 0);color: rgb(255, 255, 255);}QPushButton:hover{background-color: rgb(150, 30, 0);color: rgb(255, 255, 0);}QPushButton:pressed{background-color: rgb(60, 60, 60);color: rgb(0, 0, 255);}"

def SetValue(Name, Value):
    _GlobalDict[Name] = Value
def GetValue(Name, DefaultValue = None):
    try:
        return _GlobalDict[Name]
    except KeyError:
        return DefaultValue


"""
    print(time.strftime("%Y%m%d"))
    StockBasicIsHs = iter(_GlobalDict["StockBasic"]["is_hs"].to_list())
    StockBasicTsCode = iter(_GlobalDict["StockBasic"]["ts_code"].to_list())
    DailyStockNum = min(len(_GlobalDict["StockBasic"]), len(_GlobalDict["DailyBasic"]))
    _GlobalDict["DailyBasic"].to_csv("../DailyBasic.csv", encoding="utf_8_sig")
    _GlobalDict["TodayAll"].to_csv("../TodayAll.csv", encoding = "utf_8_sig")
    _GlobalDict["StockBasic"].to_csv("../StockBasic.csv", encoding = "utf_8_sig")
    print(_GlobalDict["StockBasic"][_GlobalDict["StockBasic"].is_hs == "N"])
        #给今日数据添加is_hs
    _GlobalDict["DailyBasic"]["is_hs"] = None
    #循环迭代股票基础数据设定今日数据的is_hs值
    for i in range(0, len(_GlobalDict["DailyBasic"])):
        _GlobalDict["DailyBasic"].iloc[i]['is_hs'] = "N"
    _GlobalDict["DailyBasic"].to_csv("../Data/DailyBasicHS.csv", encoding="utf_8_sig")
    
    #处理股票数据,找集合
    #_GlobalDict["DailyBasic"]["name"] = None
    #_GlobalDict["DailyBasic"]["industry"] = None
    StockBasicTsCode = _GlobalDict["StockBasic"]["ts_code"].to_list()

    for DailyBasicRow in _GlobalDict["DailyBasic"].itertuples():
        if getattr(DailyBasicRow, 'ts_code') in StockBasicTsCode:
            pass
            #print(getattr(DailyBasicRow, 'ts_code'), " --> ", getattr(DailyBasicRow, 'turnover_rate'))
"""