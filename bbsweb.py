from bottle import route, run, template, static_file
import os

@route('/')
@route('/bbs')
@route('/bbs/<user>')
def welcome(user="Guest"):
	return template("Welcome back {{user}}. We're glad to see you come back.", user=user)

@route('/bbs/help')
def commands():
    return static_file("commands.txt", root=os.getcwd()+'/text')

@route('/bbs/story')
def story():
    return static_file("story.txt", root=os.getcwd()+'/text')

@route('/bbs/cwd')
def cwd():
    return os.getcwd()

@route('/bbs/terminal')
def commands():
    return static_file("terminal.html", root=os.getcwd()+'/html')

run(host='localhost', port=8080, debug=True)
