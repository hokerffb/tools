#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

"""
bhclient:
A multi thread connection test tool for tcp
by 0xFF[pengyuwei@gmail.com] 2011-1-26
version 0.01 update 2011-1-26
usage:
    create a configuration file named test_ssh.conf

    start ssh test and display nothing:
    ./bhclient.py

    runtime quit: Ctrl+\
"""

import sys
import time
import traceback
from socket import *
from threading import *

from appset import *
from common import *


def show_usage():
    print __doc__


class bh_client(Thread):
    running = True
    success_count = 0
    failed_count = 0
    error_count = 0
    
    def __init__(self, cfg, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, verbose)
        self.cfg = cfg
        self.flow = 0
    def run(self):
        try:
            self.do_connect(self.cfg)
        except:
            bh_client.error_count += 1
            f = open('./bhclient.log','a')
            traceback.print_exc(file=f)
#            f.flush()
            f.close()
    def do_connect(self, cfg):
        print "connect %s:%d" % (cfg.server_ip, cfg.server_port)
        BUFSIZ = 1024
        ADDR = (cfg.server_ip, cfg.server_port)
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        
        tcpCliSock.setblocking(0)
        tcpCliSocks.settimeout(1)

        while True:
            #data = raw_input('> ')
            #if not data:
            #    break
            data = "[BH]%s" % '*' * cfg.bhclient_flow
            print "send %s" %(data)
            tcpCliSock.send(data)
            time.sleep(1)
            data = tcpCliSock.recv(1024)
            if data:
                print data
        tcpCliSock.close()
            
def main():
    conf_file = AppSet.default_file
    
    for i in sys.argv[1:]:
        if i == '--help' or i == '-h':
            show_usage()
            sys.exit(0)
        elif i == '-c':
            conf_file = sys.argv[2]
            
    cfg = AppSet.getInstance()
    cfg.load(conf_file)
    cfg.server_ip
    cfg.server_port
    thread_count = cfg.bhclient_count
    
    while(bh_client.running):
        threads = []
        
        for i in range(0, thread_count):
            thread = bh_client(cfg)
            thread.setName("C" + str(i + 1))
            thread.start()
            threads.append(thread)
            time.sleep(cfg.get_thread_delay())

        alive_count = thread_count
        while alive_count > 0:
            for t in threads:
                t.join(timeout=1)
                if not t.isAlive(): 
                    alive_count -= 1
            time.sleep(120)
    
if __name__ == "__main__":
    main()
