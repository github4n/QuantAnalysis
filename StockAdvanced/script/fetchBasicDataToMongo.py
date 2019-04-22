from quantdata import logger
from quantdata.stock import quotes
from quantdata.db.mongo import Mongo
import threading
import time


def batchUpdateMainReport(stockCodeList):

    LOGGER_NAME = "UPDATE_DATA"
    mylog = logger.getLogger(LOGGER_NAME)
    mongodb = Mongo()
    for code in stockCodeList:
        time.sleep(1)
        mylog.info("update mainreport data of %s"%(code))
        mongodb.updateMainReport(code)

def run():

    stockList = quotes.get_stock_hq_list()
    stockCodeListAll = [stockList['code'][i:i + 100] for i in range(0, len(stockList['code']), 100)]
    threadList = []
    for stockCodeList in stockCodeListAll:
        t = threading.Thread(target=batchUpdateMainReport,args=[stockCodeList,])
        threadList.append(t)
    for t in threadList:
        t.start()
    for t in threadList:
        t.join()
        
if __name__ == '__main__':
    
    run()