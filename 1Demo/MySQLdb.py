# -*- coding: utf-8 -*-

'''
使用这种数据库接口大多是就是执行连接数据库->执行query->提取数据->关闭连接 这几个步骤。MySQLdb提供比较关键的对象，分别是Connection、Cursor、Result。。
1、虽然在MySQLdb.Connect(host ,user , passw , db)函数中，我们经常使用的只是这几个参数，但是其实里面还有很多比如字符集、线程安全、ssl等也都是很重要的参数，使用时要身份注意。
2、当使用Connection.query()函数进行query后，connection 对象可以返回两种result，分别是store_result和use_result，store_result 将结果集存回client端，而use_result则是结果集保存在server端，并且维护了一个连接，会占用server资源。此时，不可以进行任何其他的查询。建议使用store_result，除非返回结果集（result set）过大或是无法使用limit的情形。
3、提取（fetch）数据的返回形式大多有三种情形。
as a tuple(how=0) ；as dictionaries, key=column or table.column if duplicated(how=1)；as dictionaries, key=table.column (how=2)
4、每次fetch，在result内部都会产生数据位置的移动，也就是说假如有10行数据，执行result.fetch_row(3,0)，会得到前三行，再执行result.fetch_row(3,0)，
则会得到中间的三行，所以说fetch会导致position的移动。另外值得注意的是，如果使用use_result，也就是数据存储在server时，在fetch所有的条目之前，不能进行任何的query操作。
5、mysql本身不支持游标（Cursor），但是MySQLdb对Cursor进行了仿真。重要的执行query方法有execute 和 executemany 。
execute方法，执行单条sql语句，调用executemany方法很好用，数据库性能瓶颈很大一部分就在于网络IO和磁盘IO将多个insert放在一起，只执行一次IO，可以有效的提升数据库性能。
游标cursor具有fetchone、fetchmany、fetchall三个方法提取数据，每个方法都会导致游标游动，所以必须关注游标的位置。
游标的scroll(value, mode)方法可以使得游标进行卷动，mode参数指定相对当前位置(relative)还是以绝对位置(absolute)进行移动。
6、MySQLdb提供了很多函数方法，在官方指南里没有完全罗列，使用者可以用help去看看，里面提供了很多方便的东西。
7、对于mysql来说，如果使用支持事务的存储引擎，那么每次操作后，commit是必须的，否则不会真正写入数据库，对应rollback可以进行相应的回滚，但是commit后是无法再rollback的。
commit() 可以在执行很多sql指令后再一次调用，这样可以适当提升性能。
8、executemany处理过多的命令也不见得一定好，因为数据一起传入到server端，可能会造成server端的buffer溢出，而一次数据量过大，也有可能产生一些意想不到的麻烦
。合理，分批次executemany是个不错的办法。
# -*- coding: cp936 -*-
#http://sourceforge.net/projects/mysql-python/files/latest/download
#$ tar xfz MySQL-python-1.2.3.tar.gz
#$ cd MySQL-python-1.2.3
#$ python setup.py build
#$ sudo python setup.py install
import MySQLdb as mdb
con = None
try:
    con = mdb.connect(host='localhost',user='root',passwd='123456',db='DZMS',charset='utf8');
    cur = con.cursor()#所有的查询，都在连接con的一个模块cursor上面运行的
    cur.execute("SELECT VERSION()")#执行一个查询
    data = cur.fetchone()#取得上个查询的结果，是单个结果
    print "Database version : %s " % data
    cur.close()
    
    cursor = conn.cursor()             
    sql = "insert into user(name,created) values(%s,%s)"    
    param = ("aaa",int(time.time()))     
    n = cursor.execute(sql,param)
    print n
    con.commit()
finally:
    if con: #无论如何，连接
        con.close()

#首先,我们用使用连接对象获得一个cursor对象,接下来,我们会使用cursor提供的方法来进行工作.
#这些方法包括两大类:1.执行命令,2.接收返回值
#cursor用来执行命令的方法:
callproc(self, procname, args)#用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
execute(self, query, args)#执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
executemany(self, query, args)#执行单条sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
nextset(self)#移动到下一个结果集
#cursor用来接收返回值的方法:
fetchall(self)#接收全部的返回结果行.
fetchmany(self, size=None)#接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
fetchone(self)#返回一条结果行.
scroll(self, value, mode='relative')#移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一行移动value条.
下面的代码是一个完整的例子.
#使用sql语句,这里要接收的参数都用%s占位符.要注意的是,无论你要插入的数据是什么类型,占位符永远都要用%s
sql="insert into cdinfo values(%s,%s,%s,%s,%s)"
#param应该为tuple或者list
param=(title,singer,imgurl,url,alpha)
#执行,如果成功,n的值为1
n=cursor.execute(sql,param)
#再来执行一个查询的操作
cursor.execute("select * from cdinfo")
#我们使用了fetchall这个方法.这样,cds里保存的将会是查询返回的全部结果.每条结果都是一个tuple类型的数据,这些tuple组成了一个tuple
cds=cursor.fetchall()
#因为是tuple,所以可以这样使用结果集
print cds[0][3]
#或者直接显示出来,看看结果集的真实样子
print cds
#如果需要批量的插入数据,就这样做
sql="insert into cdinfo values(0,%s,%s,%s,%s,%s)"
#每个值的集合为一个tuple,整个参数集组成一个tuple,或者list
param=((title,singer,imgurl,url,alpha),(title2,singer2,imgurl2,url2,alpha2))
#使用executemany方法来批量的插入数据.这真是一个很酷的方法!
n=cursor.executemany(sql,param)
#需要注意的是(或者说是我感到奇怪的是),在执行完插入或删除或修改操作后,需要调用一下conn.commit()方法进行提交.
#这样,数据才会真正保存在数据库中.我不清楚是否是我的mysql设置问题,
#总之,今天我在一开始使用的时候,如果不用commit,那数据就不会保留在数据库中,但是,数据确实在数据库呆过.
#因为自动编号进行了累积,而且返回的受影响的行数并不为0.
cursor.close()#需要分别的关闭指针对象和连接对象.他们有名字相同的方法
conn.close()
'''


