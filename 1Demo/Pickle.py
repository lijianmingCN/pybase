# -*- coding: utf-8 -*-
#pickle 对象串行化
'''
pickle.dump(obj, file, [,protocol])
　　注解：将对象obj保存到文件file中去。
　　　　　protocol为序列化使用的协议版本，0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；
        1：老式的二进制协议；2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为3。
　　　　　file：对象保存到的类文件对象。
        file必须有write()接口， file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。
        文件对象需要是二进制模式打开的。
　　pickle.load(file)
　　注解：从file中读取一个字符串，并将它重构为原来的python对象。
　　file:类文件对象，有read()和readline()接口。
'''

try:
    import cPickle as pickle
except:
    import pickle
#编码和解码字符串
data = [{'a':'A','b':'B','c':'C'}]
data_string = pickle.dumps(data)
print "%r" % data_string
data = pickle.loads(data_string)
print data

#处理流
from StringIO import StringIO
class SimpleObject(object):
    def __init__(self,name):
        self.name = name
        self.name_backwards = name[::-1]
        return
data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))
out_s = StringIO()
for o in data:
    print '%s(%s)'%(o.name,o.name_backwards)
    pickle.dump(o,out_s)
    out_s.flush()
in_s = StringIO(out_s.getvalue())
while True:
    try:
        o=pickle.load(in_s)
    except EOFError:
        break
    else :
        print '%s(%s)'%(o.name,o.name_backwards)
        
#重构对象的问题


#不可pickle对象
#循环引用

#持久化类对象和列表对象
import pickle

class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print( self.name+"_"+str(self.age) )

aa = Person("JGood", 2)
aa.show()
f=open('p.txt','wb')  #必须以二进制打开，否则有错
pickle.dump(aa,f,0)

l1 = [ 1, 2, 3 ]
pickle.dump( l1, f, 0 )
f.close()    #必须先关闭，否则pickle.load(f1)会出现EOFError: Ran out of input

f=open('p.txt','rb')
bb=pickle.load(f)
bb.show()

l2 = pickle.load(f)
print(l2)
f.close()
