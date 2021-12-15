#!/usr/bin/python3

from random import randint
import os
import socket
import time

REMOTE_ADDR = "106.52.124.182"
REMOTE_USER = "lighthouse"
REMOTE_PORT = 22

START_PORT = 6000
END_PORT = 7000

def generate_port():
    for i in range(END_PORT - START_PORT):
        port = randint(START_PORT, END_PORT)
        if not is_port_open(port):
            return port
        time.sleep(0.1)
    return -1

def is_port_open(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    # returns an error indicator
    result = s.connect_ex((REMOTE_ADDR, port))
    s.close()
    print(f'result:{result}')
    return result == 0

def remote():
    port = generate_port()
    if port != -1:
        command = f'autossh -v -o "ExitOnForwardFailure=yes" -CNR 0.0.0.0:{port}:0.0.0.0:22 {REMOTE_USER}@{REMOTE_ADDR}'
        print(command)
        print(f"remote at port {port}")
        os.system(command)
    else:
        print(f"can't remote at server {START_PORT}-{END_PORT}")

if __name__ == "__main__":
    remote()
