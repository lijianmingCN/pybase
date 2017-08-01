# -*- coding: utf-8 -*-
import urllib
#f = urllib.urlopen('http://tieba.baidu.com/')
#print f.info()#返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
#print f.getcode()#返回Http状态码
#print f.url#返回请求的url
#print f.readlines()

#urllib.urlcleanup()#由于urllib.urlretrieve()所产生的缓存

'''
#GET
params=urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
print params
f=urllib.urlopen("http://python.org/query?%s" % params)
print f.read()
'''
#POST
params = urllib.urlencode({'user_id':1387397198,'tbs':'9dc35a4bd0a547a51476014136','BDUSS':'N5ZlNQRWhsT3dlbjktN212Wms5YkNsRGtNd01lVktBaTdnbXhDZmVEczN2U0ZZQVFBQUFBJCQAAAAAAAAAAAEAAABOALJSTmlrbGF1c19MaQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcw-lc3MPpXS3'})
params = 'sign=3573787D80239B8C494FF7EF4FC5AD57&brand_type=iPhone%206&_timestamp=1476014137280&brand=iPhone&_client_version=1.2.0&from=appstore&user_id=1387397198&cuid=563FB165758E8FA9A71279BCB7F59FCF%7Ccom.baidu.tbclientala&subapp_type=ala&_phone_imei=563FB165758E8FA9A71279BCB7F59FCF&_os_version=10.0.2&BDUSS=N5ZlNQRWhsT3dlbjktN212Wms5YkNsRGtNd01lVktBaTdnbXhDZmVEczN2U0ZZQVFBQUFBJCQAAAAAAAAAAAEAAABOALJSTmlrbGF1c19MaQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcw-lc3MPpXS3&tbs=9dc35a4bd0a547a51476014136&_phone_newimei=563FB165758E8FA9A71279BCB7F59FCF&_client_type=1'
params = 'sign=3573787D80239B8C494FF7EF4FC5AD57&brand_type=iPhone%206&_timestamp=1476014137280&brand=iPhone&_client_version=1.2.0&from=appstore&user_id=1387397198&cuid=563FB165758E8FA9A71279BCB7F59FCF%7Ccom.baidu.tbclientala&subapp_type=ala&_phone_imei=563FB165758E8FA9A71279BCB7F59FCF&_os_version=10.0.2&BDUSS=N5ZlNQRWhsT3dlbjktN212Wms5YkNsRGtNd01lVktBaTdnbXhDZmVEczN2U0ZZQVFBQUFBJCQAAAAAAAAAAAEAAABOALJSTmlrbGF1c19MaQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcw-lc3MPpXS3&tbs=9dc35a4bd0a547a51476014136&_phone_newimei=563FB165758E8FA9A71279BCB7F59FCF&_client_type=1'
f=urllib.urlopen("http://c.tieba.baidu.com/ala/user/center",params)
print f.read()