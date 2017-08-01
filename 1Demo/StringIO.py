# -*- coding: utf-8 -*-
#7.5. StringIO �� Read and write strings as files
'''
StringIO经常被用来作为字符串的缓存，应为StringIO有个好处，
他的有些接口和文件操作是一致的，也就是说用同样的代码，可以同时当成文件操作或者StringIO操作。
因为文件对象和StringIO大部分的方法都是一样的，
比如read, readline, readlines, write, writelines都是有的，
这样，StringIO就可以非常方便的作为"内存文件对象"。
'''
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO


output = StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
print output.getvalue()
# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

input = StringIO('third line.\n')
print input.read()
