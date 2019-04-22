
from quantdata.analyze import AbstractAnalyze
from quantdata.stock import quotes
from quantdata import logger
from quantdata.db.mysql import Mysql
from operator import itemgetter

class GuaidianAnalyze(AbstractAnalyze):

    def __init__(self):
        self.__logger = logger.getLogger("Guaidian")

    def get_code_list(self):
        try:
            stock_list = quotes.get_stock_hq_list()
            return stock_list["code"].tolist()
        except Exception as e:
            self.__logger.error(e)
            return []

    def analyze_data(self,code):
        '''连续三年业绩增长都小于30%，最近3个季度业绩增长大于30%'''
        db = Mysql()
        report_list = db.select("select * from mainreport where code = %s order by ke_mu_shi_jian desc"%(code))
        if isinstance(report_list,list) and len(report_list) > 0:
            report_list_year = list(filter(lambda x: x["ke_mu_shi_jian"].find("12-31") != -1, report_list))
            report_list_des = sorted(report_list, key=itemgetter("ke_mu_shi_jian"), reverse=True)
            report_list_year_des =  sorted(report_list_year, key=itemgetter("ke_mu_shi_jian"), reverse=True)
            last_three_quarter_report_list = report_list_des[-3:]
            if last_three_quarter_report_list[-1]["ke_mu_shi_jian"].find("12-31") != -1:
                last_three_year_report_list = report_list_year_des[-4:-1]
            else:
                last_three_year_report_list = report_list_year_des[-3:]


            '''3年增长率小于30%'''
            for report in last_three_year_report_list:
                if report['jing_li_run_tong_bi_zeng_zhang_lv'] < '30':
                    continue
                else:
                    return False,report_list
            '''最近3季度增长率大于30%'''
            for report in last_three_quarter_report_list:
                if report['jing_li_run_tong_bi_zeng_zhang_lv'] > '30':
                    continue
                else:
                    return False,report_list
            return True,report_list
        return False,None


    def store_success_result(self,data):
        print("success code:%s"%(data[0]['code']))
    def store_fail_result(self,data):
        if data is not None:
            print("fail code:%s" % (data[0]['code']))

if __name__ == "__main__":
    ana = GuaidianAnalyze()
    ana.run(100)
