# -*- coding: utf-8 -*-
'''
zipfile 模块可以让你打开或写入一个 zip 文件。比如：
import zipfile
z = zipfile.ZipFile('zipfilename', mode='r')
  这样就打开了一个 zip 文件，如果mode为'w'或'a'则表示要写入一个 zip 文件。如果是写入，则还可以跟上第三个参数：
  compression=zipfile.ZIP_DEFLATED 或
  compression=zipfile.ZIP_STORED ZIP_DEFLATED是压缩标志，如果使用它需要编译了zlib模块。而后一个只是用zip进行打包，并不压缩。
在打开了zip文件之后就可以根据需要是读出zip文件的内容还是将内容保存到 zip 文件中。
读出zip中的内容
很简单，zipfile 对象提供了一个read(name)的方法。name为 zip文件中的一个文件入口，执行完成之后，将返回读出的内容，你把它保存到想到的文件中即可。
写入zip文件
有两种方式，一种是直接写入一个已经存在的文件，另一种是写入一个字符串。
对 于第一种使用 zipfile 对象的 write(filename, arcname, compress_type)，后两个参数是可以忽略的。第一个参数是文件名，第二个参数是表示在 zip 文件中的名字，如果没有给出，表示使用与filename一样的名字。compress_type是压缩标志，它可以覆盖创建 zipfile 时的参数。第二种是使用 zipfile 对象的 writestr(zinfo_or_arcname, bytes)，第一个参数是zipinfo 对象或写到压缩文件中的压缩名，第二个参数是字符串。使用这个方法可以动态的组织文件的内容。
需要注意的是在读出时，因为只能读出内容，因此如果想实现按目录结构展开 zip 文件的话，这些操作需要自已来完成，比如创建目录，创建文件并写入。而写入时，则可以根据需要动态组织在 zip 文件中的目录结构，这样可以不按照原来的目录结构来生成 zip 文件。
'''
#打包成zip文件
import zipfile,os
f = zipfile.ZipFile('Dbm.zip','w',zipfile.ZIP_DEFLATED)
f.write('Dbm.py')
f.close() 

#从zip文件解包 
import zipfile 
zfile = zipfile.ZipFile('Anydbm.zip','r') 
for filename in zfile.namelist(): 
    data = zfile.read(filename) 
    file = open(filename, 'w+b') 
    file.write(data) 
    file.close() 

#把整个文件夹内的文件打包 
import zipfile 
f = zipfile.ZipFile('libs.zip','w',zipfile.ZIP_DEFLATED) 
startdir = "C:\\DevelopFolder\\lib\\" 
for dirpath, dirnames, filenames in os.walk(startdir): 
    for filename in filenames: 
        f.write(os.path.join(dirpath,filename)) 
f.close() 



