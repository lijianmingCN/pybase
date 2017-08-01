# -*- coding: utf-8 -*-
#15.7. logging — Logging facility for Python
'''
Logging库被设计成模块的方式,它提供了以下几个子模块:
Loggers把应用需要直接调用的接口暴露出来.
Handlers把log记录发到相应的目的地.
Filters决定哪些记录需要发给handler.
Formatters定义了log记录的输出格式.

Logger对象扮演了三重角色.
首先,它暴露给应用几个方法以便应用可以在运行时写log.
其次,Logger对象按照log信息的严重程度或者根据filter对象来决定如何处理log信息(默认的过滤功能).
最后,logger还负责把log信息传送给相关的loghandlers.
Logger中最长使用的方法分成两部分中:configuration和message sending.
用于Configuration的方法:
setLevel(level) 
addFilter(filter) 
removeFilter(filter) 
addHandler(handler) 
removeHandler(handler) 

setLevel()方法定义了一个logger处理的最底严重程度
(比如说中/高/底三种,我定义为中,那么只有严重程度为中或者高的log才会被处理).
如果严重级别设为info级,logger仅仅处理info,warning,error和critical级的log,而debug级别的则忽略掉.
根据logger对象的设置,以下的方法被用来写log:
debug(log_message, [*args[, **kwargs]]) 
info(log_message, [*args[, **kwargs]]) 
warning(log_message, [*args[, **kwargs]]) 
error(log_message, [*args[, **kwargs]]) 
critical(log_message, [*args[, **kwargs]]) 
exception(message[, *args]) 
log(log_level, log_message, [*args[, **kwargs]]) 

debug(),info(),warning(),error()和critical()方法用一个log_message格式字符串和与之对应的各个参数来生成log信息.
log_message实际上是一个格式字符串,它可以包含诸如%s,%d,%f此类的替换符号.*args是实际要替换%s,%d,%f参数的列表.
至于这个**kwargs关键字参数,logging只处理一个关键字exc_info,这个关键字决定是否对异常信息打log.

exception()跟error()方法基本一样.不同之处是exception()多出一个stack trace用于转储.exception()方法只能从一个exception handler里面调用.
Log()方法显式的带一个level参数,用这个可以得到比使用上面所列举的方法更为详细的log信息,这属于自定义log信息的范畴了.
Logging.getLogger([name])方法返回一个logger实例的引用,如果name参数给出,则用这个参数的值作为名字,如果没有则用root做默认值.
名字是以点号分割的命名方式命名的(a.b.c).对同一个名字的多个调用logging.getLogger()方法会返回同一个logger对象.
这种命名方式里面,后面的loggers是前面logger的子.比如说,有一个名字是foo的logger,那么诸如foo.bar,foo.bar.baz和foo.bam
这样的logger都是foo这个logger的子loggers自动继承父loggers的log信息,正因为此,没有必要把一个应用的所有logger都配置一边,
只要把顶层的logger配置好了,然后子logger根据需要继承就行了.

Handler对象负责分配合适的log信息(基于log信息的严重程度)到handler指定的目的地.
Logger对象可以用addHandler()方法添加零个或多个handler对象到它自身.
一个常见的场景是,一个应用可能希望把所有的log信息都发送到一个log文件中去,所有的error级别以上的log信息都发送到stdout,
所有critical的log信息通过email发送.这个场景里要求三个不同handler处理,每个handler负责把特定的log信息发送到特定的地方.

标准库里面包括以下的handlers:
StreamHandler 
FileHandler 
RotatingFileHandler 
TimedRotatingFileHandler 
SocketHandler 
DatagramHandler 
SysLogHandler 
NTEventLogHandler 
SMTPHandler 
MemoryHandler 
HTTPHandler 

Handler里面提供给应用开发者的只有很少的几个方法可用.对使用内置的handler(就是说不是自定义的handlers)的开发者可用的配置方法如下:
setLevel(level) 
setFormatter(formatter) 
addFilter(filter) 
removeFilter(filter) 

setLevel()方法跟logger对象里面的setLevel()一样,也是用于设定一个最低分发log信息的级别.为什么有两个setLevel()呢?
logger的严重等级用于决定那个级别的log信息可以分发到它的handlers.handler里面的level设置用于控制那些个log信息是handler需要转寄的.
setFormatter()方法选定一个格式化对象给它自己用.addFilter()和removeFilter()分别用于为handler增加一个filter和删除一个filter.

应用里面Handler不应该被直接实例化.相反,应该用logging.Handler类作所有Handlers的基类,在它里面定义所有自Handler用到的接口并且创建一些默认的方法让子类来用(或者继承).
'''

import logging
import sys
logger = logging.getLogger("endlesscode")
formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s')
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
logger.error("ABC")
logger.removeHandler(stream_handler)
logger.error("OPQ")

import logging
from logging.handlers import RotatingFileHandler

#################################################################################################
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)

