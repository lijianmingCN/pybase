# -*- coding:UTF-8 -*-
#https://github.com/andymccurdy/redis-py
import redis

#链接Redis
client = redis.Redis(host='123.57.230.194',port=9001,db=0)
#基本信息
info = client.info()
for key in info: 
   print "%s: %s" % (key, info[key])
print 'DBsize:'+str(client.dbsize()) #数据库大小
print 'time:'+str(client.time()) #时间
print "ping："+str(client.ping()) #连接状态
print client.set('foo','bar')
print client.get('foo')
print client.delete('foo')
print client.get('foo')
print client.lastsave() # 取最后一次save时间 
print client.save()   #强行把数据库保存到硬盘。保存时阻塞
print client.flushdb()   #删除当前数据库的所有数据
client.connection_pool.disconnect()

print '-'*20
#线程池
pool = redis.ConnectionPool(host='123.57.230.194', port=9001, db=0)
r = redis.Redis(connection_pool=pool)
print r.set('foo', 'bar')
print r.get('foo')
print r.delete('foo')
print r.get('foo')
r.flushdb()
r.connection_pool.disconnect()
#Redis client instances can safely be shared between threads

print '-'*20
#Pipelines
r.set('bing', 'baz')
# Use the pipeline() method to create a pipeline instance
pipe = r.pipeline()
# The following SET commands are buffered
pipe.set('foo', 'bar')
pipe.get('bing')
# the EXECUTE call sends all buffered commands to the server, returning
# a list of responses, one for each command.
pipe.execute()
pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()



