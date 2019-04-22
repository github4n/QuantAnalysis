from abc import ABCMeta, abstractmethod
import threading,time


class AbstractAnalyze(object):

    __metaclass__  = ABCMeta


    @abstractmethod
    def get_code_list(self):
        """
        返回要分析的代码列表
        :return: list
        """
        raise NotImplementedError("Should implement get_code_list()")

    @abstractmethod
    def analyze_data(self,code):
        """
        更新某代码的数据
        :param code:
        :return:(boolean,dict)
        """
        raise NotImplementedError("Should implement analyze_data()")

    def store_success_result(self,data):
        """
        保存分析后满足条件的结果
        :param data: 分析结果
        :return:
        """
        raise NotImplementedError("Should implement store_success_result()")

    def store_fail_result(self,data):
        """
        保存分析后不满足条件的结果
        :param data: 分析结果
        :return:
        """
        raise NotImplementedError("Should implement store_fail_result()")

    def batch_analyze_data(self,code_list):
        """
        批量获取数据
        :param code_list:
        :return:
        """
        for code in code_list:
            if_success,result = self.analyze_data(code)
            if if_success:
                self.store_success_result(result)



    def run(self,thread_num = 100):
        """
        多线程并发获取数据
        :return:
        """
        code_list = self.get_code_list()
        all_code_list = [code_list[i:i + thread_num] for i in range(0, len(code_list), thread_num)]
        threadList = []
        for code_list_spilt in all_code_list:
            t = threading.Thread(target=self.batch_analyze_data, args=[code_list_spilt, ])
            threadList.append(t)
        for t in threadList:
            t.start()
        for t in threadList:
            t.join()