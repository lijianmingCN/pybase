# -*- coding: cp936 -*-
import memcache,time

def base():
    mc = memcache.Client(['123.57.230.194:11211'], debug=0)
    #mc = memcache.Client(['10.58.156.46:11211'], debug=0)
    #设置key和value，第三个参数默认为0，也就是数据永不超时。
    mc.set("name", "niklaus")
    #表示一秒后超时
    mc.set("address", "berjing",1)
    time.sleep(2)
    print mc.get("name")
    print mc.get("address")

    #删除
    mc.set("age", 3)
    print mc.get("age")
    mc.delete("age")
    print mc.get("age")

    #自增和自减
    mc.set("key", "1")                                                                                
    mc.incr("key")
    print mc.get("key")
    mc.decr("key")
    print mc.get("key")
    
def getStat():
    mc = memcache.Client(['123.57.230.194:11211'], debug=0)
    for l in mc.get_stats():
        print 'host:'+l[0]
        for d in l[1:]:
            for key in d.keys():
                print key+'  '+d[key]

def getSlabs():
    mc = memcache.Client(['123.57.230.194:11211'], debug=0)
    name = mc.get_slabs()[0][0]
    slab = mc.get_slabs()[0][1]
    for s in slab:
        print s
        for ss in slab[s]:
            print ss + ' : ' +slab[s][ss]
            
       
                
if __name__ == '__main__':
    getStat()
    print '------------------------------------------'
    getSlabs()
    
