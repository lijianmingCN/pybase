# -*- coding: utf-8 -*-
from bottle import route,run,template,get,post,request,response,static_file,error,abort,redirect

@route('/index')
def index():
    return "Hi 码农！！！"

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/login') # or @route(’/login’) 
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form> 
        '''

@post('/login') # or @route(’/login’, method=’POST’)
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    print username
    print password
    if username == password:
        return "<p>Your login information was correct.</p>" 
    else:
        return "<p>Login failed.</p>"




@route('/static/js/<filename>') 
def server_static(filename):
    return static_file(filename,root='./static/js')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")

@route('/wrong/url')
def wrong():
    redirect("/login")
    
@route('/iso')
def get_iso():
    response.charset = 'ISO-8859-1'
    return u'This will be sent with ISO-8859-15 encoding.'

@route('/image/<filename:re:.*\.png>') 
def send_image(filename):
    return static_file(filename, root='./image', mimetype='image/png')

@route('/file/<filename:path>') 
def send_static(filename):
    return static_file(filename, root='./file')

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='./file', download=filename)




run(host='0.0.0.0', port=8080)

