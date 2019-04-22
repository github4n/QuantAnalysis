# -*- coding:utf-8 -*-
import pymysql
import pymysql.cursors
from quantdata.stock import basic
from quantdata import cons as ct
from quantdata.db import Database

class Mysql(Database):
    
    def __init__(self):
        self.__host = ct.MYSQL_HOST
        self.__port = ct.MYSQL_PORT
        self.__database = ct.MYSQL_DATABASE
        self.__user = ct.MYSQL_USER
        self.__password = ct.MYSQL_PASSWD

        self.__date_fmt = '%Y-%m-%d'
        self.__instrumentIds = {}
        self.__open()
        
    def __open(self,autoCommit=True):
        
        try:
            self.__connection = pymysql.connect(
                                                host=self.__host, #设置MYSQL地址 
                                                port=self.__port, #设置端口号 
                                                user=self.__user, #设置用户名 
                                                passwd=self.__password, #设置密码 
                                                db=self.__database, #数据库名 
                                                charset='utf8', #设置编码
                                                cursorclass=pymysql.cursors.DictCursor
                                                )
            self.__session = self.__connection.cursor()
            if autoCommit == True:
                self.autoCommit(1)
            self.set_name()
        except Exception as e:
            print(e)
        except ZeroDivisionError as e:
            pass

    def reConnect(self):
        try:
            self.__connection.ping()
        except:
            self.__open()
        
        
    def __escape(self,value):
        return pymysql.escape_string(value)
    
    def set_name(self):
        self.query("SET NAMES utf8")
        self.query("SET CHARACTER SET utf8")
    def query(self,sql):
        try:
            self.__session.execute(sql)
            self.__connection.commit()
        except Exception as e:
            print("query error %s"%(e))
            self.reConnect()
    
    
    def insert(self,table,data):
        for key in data:
            data[key] = self.__escape(data[key])
        key   = "`,`".join(data.keys())
        value = "','".join(data.values())
        real_sql = "INSERT INTO " + table + " (`" + key + "`) VALUES ('" + value + "')"
        self.query("set names 'utf8'")
        return self.query(real_sql)
 
    def replace(self,table,data):
        for key in data:
            data[key] = self.__escape(data[key])
        key   = "`,`".join(data.keys())
        value = "','".join(data.values())
        real_sql = "REPLACE INTO " + table + " (`" + key + "`) VALUES ('" + value + "')"
        self.query("set names 'utf8'")
        return self.query(real_sql)
 
 
    def update(self,table,data,where):
        for key in data:
            data[key] = self.__escape(data[key])
        for key in where:
            where[key] = self.__escape(where[key])
        edit_sql  = ",".join([str(x[0])+"='"+str(x[1])+"'" for x in data.items()])
        where_sql = " AND ".join([str(x[0])+"='"+str(x[1])+"'" for x in where.items()])
        real_sql = "UPDATE "+table+" SET "+edit_sql+" WHERE "+where_sql
        self.query("set names 'utf8'")
        return self.query(real_sql)
    def delete(self,table,where):
        for key in where:
            where[key] = self.__escape(where[key])
        where_sql = " AND ".join([x[0]+"='"+x[1]+"'" for x in where.items()])
        real_sql  = "DELETE FROM "+table+" WHERE "+where_sql
        self.query("set names 'utf8'")
        return self.query(real_sql)
     
    def isinstance(self,table,where):
        for key in where:
            where[key] = self.__escape(where[key])
        where_sql = " AND ".join([x[0]+"='"+x[1]+"'" for x in where.items()])
        real_sql = "SELECT count(*) as cnt FROM "+table+" WHERE "+where_sql
        if self.query(real_sql):
            res = self.fetchAssoc()
            return res['cnt']
        else:
            return 0
        
    def select(self,sql):
        self.query("set names 'utf8'")
        self.query(sql)
        return self.fetchAll()
 
 
    def selectRow(self,sql):
        self.query("set names 'utf8'")
        self.query(sql)
        return self.fetchAssoc()
    
    def fetchAll(self,upper=0):
        if self.get_num_rows():
            result=self.__session.fetchall()
            return result
        else:
            return None
        
    def fetchAssoc(self,upper=0):
        if self.get_num_rows():
            self.fields = self.__session.fetchone()
            return self.fields
        else:
            return None
    def get_num_rows(self):
        return self.__session.rowcount

    def get_tables(self):
        """
        获取所有表
        :return: list tableList
        """
        rs = self.select("show tables")
        tableList = []
        for rsDict in rs:
            for _, v in rsDict.items():
                tableList.append(v)
        return tableList
    def get_columns(self,table):
        """
        :param table:
        :return: columns
        """
        rs = self.select("SHOW COLUMNS FROM %s"%(table))
        colmunList = []
        if rs is not None:
            for item in rs:
                colmunList.append(item["Field"])
        return colmunList
    def add_columns(self,table,columns_list):
        columns_sql = ",".join([column['name'] + " " + column['type'] + " default null COMMENT '" + self.__escape(column['comment']) + "'" for column in columns_list if 'name' in column and 'type' in column and 'comment' in column])
        if len(columns_sql) == 0:
            print("no column add")
            return None
        real_sql = "alter table " + table + " add  ( " + columns_sql + ")"
        self.query("set names 'utf8'")
        return self.query(real_sql)

    def add_table_not_exists(self,table):
        tableList = self.get_tables()
        if table not in tableList:
            sql = "CREATE TABLE  IF NOT EXISTS "+table+" (`id` INT UNSIGNED AUTO_INCREMENT,`code` varchar(50) default null,PRIMARY KEY ( `id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;"
            self.query(sql)


    
    def error(self,e):
        print("Error %d: %s" % (e.args[0], e.args[1]))
         
        
    def getInsertId(self):
        self.query("SELECT LAST_INSERT_ID() AS lid")
        rs = self.__session.fetchone()
        return rs[0]
     
    def commit(self):
        self.__connection.commit()
        
    def get_mysql_version(self):
        """return the mysql version"""
        return pymysql.get_client_info()
    
    def autoCommit(self,flag):
        self.query("Set AUTOCOMMIT = "+str(flag))
    
    def __del__(self):
        self.__session.close()
        self.__connection.close()
if __name__ == "__main__":
    
    con = Mysql()
    tables = con.get_tables()
    print(tables)
    columns = con.get_columns("mainreport")
    print(columns)