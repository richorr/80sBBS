from bottle import route, run, template, static_file
import os
import bbswelcome

@route('/')
@route('/bbs')
def welcome():
	return welcome.formatlogo("Narrative Coffee", "stampatello")

@route('/bbs/<user>')
def welcome(user="Guest"):
	return template("Welcome back {{user}}. We're glad to see you come back.", user=user)

@route('/bbs/help')
def commands():
    return static_file("commands.txt", root=os.getcwd()+'/text')

@route('/bbs/hints')
def story():
    return static_file("hints.txt", root=os.getcwd()+'/text')

@route('/bbs/terminal')
def commands():
    return static_file("bbs-terminal.html", root=os.getcwd()+'/html')

@route('/bbs/js/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.getcwd()+'/html/js')

@route('/bbs/css/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.getcwd()+'/html/css')

run(host='localhost', port=8080, debug=True)
