#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8
# create by 0xFF[pengyuwei@gmail.com] 2008-7-23
"""
the application configure class.
update by 0xFF[pengyuwei@gmail.com] 2010-12-29

test_ssh.conf example:

# ssh test tool configuration file 0.07

# total thread count
thread_count=10

# -1 = randomize delay of each thread start(0-60 seconds)
thread_delay=1

# loop start thread count, 0:loop forever
thread_loop_count=1

# loop run command's count, 0:loop forever
loop_count=2

# start scp test with scp param
scp_cmd=scp ./user.bmp root@192.168.1.1:~/
scp_pwd=<password>

# start ssh test without param
ssh_cmd=ssh root@192.168.1.1
ssh_pwd=<password>
prompt=\]\#
# for keep connection test(small interactive data)
cmd_delay=60

# ssh autorun commands
cmd=pwd
cmd=sleep 5
cmd=touch ~/1
cmd=touch ~/2
"""

import unittest
import re
import random
import base64

class AppSet:
    """Manage application configure data."""
    instance = None
    default_file = 'test_ssh.conf'

    #@staticmethod
    def getInstance():
        if AppSet.instance==None:
            AppSet.instance = AppSet()
        return AppSet.instance
    getInstance = staticmethod(getInstance)

    def __init__(self):
        self.conf_file = ''
        self.thread_count = 0
        self.thread_delay = 0
        self.sshell = ''
        self.sshell_pwd = ''
        self.scp = ''
        self.scp_pwd = ''
        self.prompt = ''
        self.loop_count = 1
        self.thread_loop_count = 1
        self.cmd_delay = 0
        self.cmds = []
        self.error_log = True
        
        self.server_ip = '127.0.0.1'
        self.server_port = 80
        self.bhclient_count = 1
        self.bhclient_flow = 1024
        
        self.regex         = re.compile(r'(\S+?)\=(.*)')
        
        self.log_level        = 0
        self.debug        = False
    
    def parse(self, line):
        if len(line) > 0:
            if '#' == line[0]:
                return
        r = self.regex.search(line)
        if None != r:
            var = r.groups()[0]
            value = r.groups()[1]
            #print '%s--> %s is %s' % (line, var, value)
            
            if "thread_count"==var:
                self.thread_count = int(value)
            elif "thread_delay"==var:
                self.thread_delay = int(value)
            elif "ssh_cmd"==var:
                self.sshell = value
            elif "ssh_pwd"==var:
                self.sshell_pwd = base64.decodestring(value)
            elif "scp_cmd"==var:
                self.scp = value
            elif "scp_pwd"==var:
                self.scp_pwd = base64.decodestring(value)
            elif "prompt"==var:
                self.prompt = value
            elif "cmd"==var:
                self.cmds.append(value)
            elif "cmd_delay"==var:
                self.cmd_delay = float(value)
            elif "loop_count"==var:
                self.loop_count = int(value)
            elif "thread_loop_count"==var:
                self.thread_loop_count = int(value)                
            elif "log_level"==var:
                self.log_level = int(value)
            elif "server_ip"==var:
                self.server_ip = value
            elif "server_port"==var:
                self.server_port = int(value)
            elif "bhclient_count"==var:
                self.bhclient_count = int(value)
            elif "bhclient_flow"==var:
                self.bhclient_flow = int(value)
            elif "debug"==var:
                if int(value)==1:
                    self.debug = True
                else:
                    self.debug = False
            
        
    def load(self, conf_file):
        self.conf_file = conf_file
        try:
            conf = open(conf_file, 'r')
            for eachline in conf:
                self.parse(eachline)
            conf.close()
        except:
            print 'Application configure load failed.\n'
            pass
            
    def get_thread_delay(self):
        if self.thread_delay >= 0:
            return self.thread_delay
        else:
            return random.randint(0,60)
        

class AppSetTest(unittest.TestCase):
    def testGetInstance(self):
        cfg = AppSet.getInstance()
        self.failIf(None == cfg)
        print 'testGetInstance \t\t[OK]'
    
    def testSshCmd(self):
        cfg = AppSet.getInstance()
        cfg.parse("ssh_cmd=ssh root@192.168.27.169")
        self.assertEqual(cfg.sshell, "ssh root@192.168.27.169")
        print 'testSshCmd \t\t\t[OK]'
    
    def testLoad(self):
        cfg = AppSet.getInstance()
        cfg.load('test_ssh.conf')
        #print 'ssh cmd is %s' % (set.sshell)
        #print 'scp cmd is %s' % (set.scp)
        #print 'thread count is %s' % (set.thread_count)
        #print 'prompt is %s' % (set.prompt)
        print '%d comamnds\n' % (len(cfg.cmds))
        print 'testLoad \t\t\t[OK]'
        

if __name__ == '__main__':
    print 'Main\n'
    unittest.main()
