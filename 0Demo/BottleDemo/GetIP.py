# -*- coding: utf-8 -*-
from bottle import route,run,template,get,post,request,response,static_file,error,abort,redirect

@route('/ip')
def getIp():
  # 获取客户端ip
  return request.environ.get('REMOTE_ADDR')

run(host='0.0.0.0', port=8080)