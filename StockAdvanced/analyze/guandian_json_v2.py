from quantdata.analyze import AbstractAnalyze
from quantdata.stock import quotes
from quantdata import logger
from quantdata.util.func import *
import pandas as pd
import numpy as np
import os
import json


class GuaidianJsonV2Analyze(AbstractAnalyze):

    def __init__(self):
        self.__logger = logger.getLogger("GuaidianJson")
        self.__data_path = './stockdata/mainreport'

    def get_code_list(self):
        try:
            stock_list = quotes.get_stock_hq_list()
            return stock_list["code"].tolist()
        except Exception as e:
            self.__logger.error(e)
            return []

    def __get_main_report_df(self,code):

        with open(os.path.join(self.__data_path,code+".json"),"r") as f:
            report_obj = json.load(f)
            colums  = [x[0] if isinstance(x, list) else x for x in report_obj['title']]
            df = pd.DataFrame(columns=colums)
            for i in range(0,len(colums)):
                df[colums[i]] = report_obj["report"][i]
            df = df.set_index(colums[0])
            df = df.sort_index(ascending=False)
            return df

    def analyze_data(self,code):
        try:
            '''寻找业绩拐点，业绩拐点波幅为50%'''
            df = self.__get_main_report_df(code)
            #获取最近3季度报表
            df_3_quarter = df.head(3)
            #获取最近3年的报表
            df_3_year = df[df.index.str.contains("-12-31")].head(3)

            for margin_incr in df_3_year['净利润同比增长率']:
                if self._to_float(margin_incr) > 40.0 or self._to_float(margin_incr) < 20.0:
                    return False,code
            for margin_incr in df_3_quarter['净利润同比增长率']:
                if self._to_float(margin_incr) < 30.0:
                    return False,code
            print(code)
            return True,code
        except Exception as e:
            self.__logger.error(e)
            return False,code

    def _to_float(self, num):
        try:
            return float(num)
        except:
            return 0.0

    def store_success_result(self,data):
        print("success code:%s"%(data))

    def store_fail_result(self,data):
        if data is not None:
            print("fail code:%s" % (data))

if __name__ == "__main__":
    ana = GuaidianJsonV2Analyze()
    ana.run(100)
