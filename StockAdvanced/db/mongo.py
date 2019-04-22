# -*- coding:utf-8 -*-
from pymongo import MongoClient
import json
from quantdata.stock import basic
from quantdata import cons as ct
from quantdata.db import Database


class Mongo(Database):
    def __init__(self):
        self.__host = ct.MONGO_HOST
        self.__port = ct.MONGO_PORT
        self.__database = ct.MONGO_DATABASE
        self.__main_report_collect = 'mainreports'
        self.__max_pool_size = 10
        self.__timeout = 10
        self.__date_fmt = '%Y-%m-%d'
        
        self.__instrumentIds = {}
        try:
            self.__connection = MongoClient(self.__host, self.__port, maxPoolSize=self.__max_pool_size,
                                            connectTimeoutMS=60 * 60 * self.__timeout)
        except Exception as e:
            print(e)

    
    def updateMainReport(self,code):
        
        try:
        
            df = basic.get_main_report(code)
            if df is None:
                return
            cursor = self.__connection[self.__database][self.__main_report_collect].find({"code":code}).sort([("date",-1)]).limit(1)
            if cursor.count() > 0:
                last_date = str(cursor[0]['date'])
                df = df[df.date > last_date]
            if not df.empty:
                df.insert(len(df.columns), "code",code)
                self.__connection[self.__database][self.__main_report_collect].insert(json.loads(df.to_json(orient='records')))
        except Exception as e:
            print(e)
            
    def getDB(self):
        return self.__connection[self.__database]
