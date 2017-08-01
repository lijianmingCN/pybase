# -*- coding: utf-8 -*-
import os
import sqlite3
'''
SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候连接对象会自动创建数据库文件；
如果数据库文件已经存在，则连接对象不会再创建数据库文件，而是直接打开该数据库文件。
连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库执行完任何操作后，都不需要提交事务的(commit)
创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
创建在内存上面： conn = sqlite3.connect(':memory:')
    其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：
        commit()            --事务提交
        rollback()          --事务回滚
        close()             --关闭一个数据库链接
        cursor()            --创建一个游标
    cu = conn.cursor()
    这样我们就创建了一个游标对象：cu
    在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
    对于游标对象cu，具有以下具体操作：
        execute()           --执行一条sql语句
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录结,果为一个tuple的列表
        scroll()            --游标滚动
'''
#DEFERRED    延迟    只有修改真正开始时时锁定数据库
#IMMEDIATE    立即    修改一开始时就会锁定数据库，事务提交之前避免其他游标修改数据库
#EXCLUSIVE    互斥    每个互斥链接都阻塞其他用户
#None    自动提交    每个execute（）调用都会在语句完成时立即提交

class DBUtils(object):
    def __init__(self,db_filename,isolation_level):
        self.db_filename = db_filename
        self.isolation_level = isolation_level
        self.conn = sqlite3.connect(self.db_filename,isolation_level = self.isolation_level)
    def __del__(self):
        self.conn.close()
    def createTableBySQL(self,schema):
        self.conn.executescript(schema)
    def insert(self,sql):
        self.conn.executescript(sql)
        self.conn.commit()
    def insertList(self,sqllist):
        for sql in sqllist:
            self.conn.executescript(sql)
        self.conn.commit()    
    def queryOne(self):
        cursor = self.conn.cursor()
        cursor.execute('select name,description,deadline from project')
        print cursor.fetchone()
        cursor.close()
    def queryAll(self):
        cursor = self.conn.cursor()
        cursor.execute('select name,description,deadline from project')
        for row in cursor.fetchall():
            print row
        cursor.close()
    def query(self,num):
        cursor = self.conn.cursor()
        cursor.execute('select name,description,deadline from project')
        for row in cursor.fetchmany(num):
            print row
        cursor.close()
    def queryByName(self,name):
        cursor = self.conn.cursor()
        sql = 'select name,description,deadline from project where name = ?'
        cursor.execute(sql,(name,))
        for row in cursor.fetchall():
            print row
        cursor.close()
    def description(self):
        cursor = self.conn.cursor()
        cursor.execute('select name,description,deadline from project')
        for colinfo in cursor.description:
            print colinfo
        cursor.close()
        
if __name__ == '__main__':
    db = DBUtils('A.db','DEFERRED')
    db.createTableBySQL("create table project(name varchar(20),description text,deadline date)")
    
    sql = '''insert into project(name,description,deadline)values('python','java','2010-11-01')'''
    db.insert(sql)
    
    sqllist = []
    sqllist.append(sql)
    sqllist.append(sql)
    sqllist.append(sql)
    db.insertList(sqllist)
    
    db.description()
    
    db.queryOne()
    db.queryAll()
    db.query(2)
    db.queryByName('python')