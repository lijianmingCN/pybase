# -*- coding: utf-8 -*-
import hashlib,os

data = 'abcd'

h = hashlib.md5()
h.update(data)
print h.hexdigest()

h = hashlib.sha1()
h.update(data)
print h.hexdigest()

h = hashlib.sha256()
h.update(data)
print h.hexdigest()



# ######## md5 ########
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
#21232f297a57a5a743894a0e4a801fc3
# ######## sha1 ########
hash = hashlib.sha1()
hash.update('admin')
print hash.hexdigest(),len(hash.hexdigest())
# d033e22ae348aeb5660fc2140aec35850c4da997 40

# ######## sha256 ########
hash = hashlib.sha256()
hash.update('admin')
print hash.hexdigest(),len(hash.hexdigest())
# 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918 64

# ######## sha384 ########
hash = hashlib.sha384()
hash.update('admin')
print hash.hexdigest(),len(hash.hexdigest())
# 9ca694a90285c034432c9550421b7b9dbd5c0f4b6673f05f6dbce58052ba20e4248041956ee8c9a2ec9f10290cdc0782 96

# ######## sha512 ########
hash = hashlib.sha512()
hash.update('admin')
print hash.hexdigest(),len(hash.hexdigest())
# c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec 128


#由于同一个消息通过摘要算法得到的摘要是相同的，因此可以通过撞库的方式得到原始消息值。解决方式是，添加一个salt拼接原始消息后再进行计算。


#大文件的MD5
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
