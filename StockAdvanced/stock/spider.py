from quantdata import logger
from quantdata.stock import quotes
from quantdata.db.mysql import Mysql
import threading
import time,json
from urllib.request import urlopen, Request
from quantdata import cons as ct
from pypinyin import lazy_pinyin

LOGGER_NAME = "SPIDER"
log = logger.getLogger(LOGGER_NAME)

def _getMainReportJson(code):
    try:
        request = Request(ct.THS_MAIN_DATA_URL % (code))
        request.add_header("User-Agent", ct.USER_AGENT)
        text = urlopen(request, timeout=ct.API_TIMEOUT).read()
        text = text.decode('gbk') if ct.PY3 else text
        reportObj = json.loads(text.strip())
        if isinstance(reportObj,dict) and "title" in reportObj and "report" in reportObj:
            return reportObj['title'],reportObj['report']
    except Exception as e:
        print(e)
def _fetchData(stockCodeList):
    db = Mysql()
    db.add_table_not_exists("mainreport")
    #拼音中文互相转换
    pinyin_2_zhongwen = {}
    zhongwen_2_pinyin = {}
    for code in stockCodeList:
        #todo:判断是否要更新当前代码是否要更新
        title, report = _getMainReportJson(code)
        _translate_title(title,pinyin_2_zhongwen,zhongwen_2_pinyin)
        exists_colnums = db.get_columns("mainreport")
        colnums = []
        for k,v in pinyin_2_zhongwen.items():
            if k not in exists_colnums:
                colnums.append({"name": k, "type": "varchar(100)", "comment": v})
        #添加缺失的列到表中
        if len(colnums) > 0:
            db.add_columns("mainreport", colnums)
        #处理report数据
        for j in range(0,len(report[0])):
            try:
                data ={}
                for i in range(0,len(report)):
                    if isinstance(title[i], str):
                        t = title[i]
                    elif isinstance(title[i], list):
                        t = title[i][0]
                    data[zhongwen_2_pinyin[t]] = str(report[i][j])
                data["code"] = code
                print(data)
                db.insert("mainreport",data)
            except Exception as e:
                print(e)
                continue

def _translate_title(title,pinyin_2_zhongwen,zhongwen_2_pinyin):
    for item in title:
        if isinstance(item,str):
            zhongwen = item
            if zhongwen in zhongwen_2_pinyin:
                continue
            else:
                pinyin = "_".join(lazy_pinyin(zhongwen, errors='ignore'))
                pinyin_2_zhongwen[pinyin] = zhongwen
                zhongwen_2_pinyin[zhongwen] = pinyin
        elif isinstance(item,list):
            zhongwen = item[0]
            zhongwen2 = item[1]
            if zhongwen in zhongwen_2_pinyin:
                continue
            else:
                pinyin = "_".join(lazy_pinyin(zhongwen, errors='ignore'))
                pinyin_2_zhongwen[pinyin] = zhongwen + "(" + zhongwen2 + ")"
                zhongwen_2_pinyin[zhongwen] = pinyin

def fetchBasicDataToMysql():
    stockList = quotes.get_stock_hq_list()
    stockCodeListAll = [stockList['code'][i:i + 100] for i in range(0, len(stockList['code']), 100)]
    threadList = []
    for stockCodeList in stockCodeListAll:
        t = threading.Thread(target=_fetchData, args=[stockCodeList, ])
        threadList.append(t)
    for t in threadList:
        t.start()
    for t in threadList:
        t.join()

if __name__ == "__main__":
    fetchBasicDataToMysql()
    #_fetchData(["600479","603168"])
    """
    title,report = _getMainReportJson("600479")
    pinyin_2_zhongwen = {}
    zhongwen_2_pinyin = {}
    for item in title:
        if isinstance(item,str):
            zhongwen = item
            if zhongwen in zhongwen_2_pinyin:
                continue
            else:
                pinyin = "_".join(lazy_pinyin(zhongwen, errors='ignore'))
                pinyin_2_zhongwen[pinyin] = zhongwen
                zhongwen_2_pinyin[zhongwen] = pinyin
        elif isinstance(item,list):
            zhongwen = item[0]
            zhongwen2 = item[1]
            if zhongwen in zhongwen_2_pinyin:
                continue
            else:
                pinyin = "_".join(lazy_pinyin(zhongwen, errors='ignore'))
                pinyin_2_zhongwen[pinyin] = zhongwen + "(" + zhongwen2 + ")"
                zhongwen_2_pinyin[zhongwen] = pinyin
    print(pinyin_2_zhongwen,zhongwen_2_pinyin)
    _fetchData([])
    """