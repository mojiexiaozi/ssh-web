from logging import log
from flask import Flask
import json
from random import randint
import socket
from threading import Lock
import os

socket.setdefaulttimeout(3) #设置默认超时时间

app = Flask(__name__)
users = dict()

PORT_START = 6000
PORT_STOP = 8000

def kill_port_thread(port):
    command='''kill -9 $(netstat -nlp | grep :'''+str(port)+''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
	
    try:
        os.system(command=command)
    except Exception as e:
        app.logger.error(e)


def is_used_port(port:int):
    """
    输入IP和端口号，扫描判断端口是否占用
    """
    try:
        if port >=65535 or port < 0:
            app.logger.warn(f'port: {port} illegal')
            return True

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(('0.0.0.0', port))
        if result == 0:
            app.logger.info(f'port: {port} used')
            return True
        
        return False
    except:
        print('端口扫描异常')

def generate_port():
    port = randint(PORT_START, PORT_STOP)
    while is_used_port(port):
        port = randint(PORT_START, PORT_STOP)
    return port

@app.route('/')
def home():
    return "<p>Hello, World!</p>"


@app.route('/getport/<username>')
def getport(username):
    if users.get(username):
        port = users[username]
    else:
        port = -1
    return str(port)

@app.route('/start/<username>')
def start(username):
    if users.get(username):
        port = users[username]
    else:
        port = randint(PORT_START, PORT_STOP)
        users[username] = port
    return str(port)

@app.route('/stop/<username>')
def stop(username):
    if users.get(username):
        kill_port_thread(users[username])
    return f'stop remote and remove port:{users[username]}'


@app.route('/lsuser')
def lsuser():
    return json.dumps(users)
