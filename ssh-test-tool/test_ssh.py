#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

"""ssh-test-tool:
A multi thread ssh connection test tool for ssh/scp
by 0xFF[pengyuwei@gmail.com] 2010-11-8
version 0.11 update 2010-12-29
usage:
    create a configuration file named test_ssh.conf

    start ssh test and display nothing:
    ./test_ssh.py

    start ssh test and use speical configure file:
    ./test_ssh.py -c <filename>

    start ssh test and display all interactive info:
    ./test_ssh.py -d

    start scp test:
    ./test_ssh.py scp

    make a password with configure file format
    ./test_ssh.py -p <password>

    force display all threads info once in runtime:
    kill -s SIGUSR1 <pid>
    
    display speical thread info use:
    kill -s SIGUSR2 <pid>
    and then input the thread index to display the info
    
    runtime quit: Ctrl+\
"""

from pexpect import *
import sys
import time
import types
import signal
import traceback
from threading import *
from appset import *
from common import *


display_detail = True
cmd_mode = False

def show_usage():
    print __doc__

class file_none(file):
    def __init__(self):
        file.__init__()
        self.size = 0
    def read(self, size):
        self.size += size
        #print "read:%d" % self.size
    def write(self, data):
        self.size += len(data)
        #print "write:%d" % self.size

class test_ssh(Thread):
    running = True
    display_all = False
    success_count = 0
    failed_count = 0
    error_count = 0
    scp = False
    
    def __init__(self, cfg, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, verbose)
        self.display = False
        self.cmds = cfg.cmds
        self.prompt = cfg.prompt
        self.cfg = cfg
        self.flow = 0
        self.ss = speed_statistics(1);
    def run(self):
        try:
            if test_ssh.scp:
                self.test_scp(self.cfg)
            else:
                self.test_sshell(self.cfg)
        except:
            test_ssh.error_count += 1
            f = open('./log','a')
            traceback.print_exc(file=f)
#            f.flush()
            f.close()
    def test_sshell(self, cfg):
        child = None
        cmdline, pwd = cfg.sshell, cfg.sshell_pwd
        
        # execute
        if test_ssh.display_all:
            child = spawn(cmdline, logfile=sys.stdout, timeout=60*5)
        else:
            #self.file_flow = file_none()
            child = spawn(cmdline, timeout=60*5)
            #child.logfile = self.file_flow
            
        # login
        ret = 0
        #print 'login, want %s\n' % self.prompt
        while ret < 2:    
            ret = child.expect(["yes/no", "password:", self.prompt, EOF, TIMEOUT, "No route to host"])
            #print 'ret = %d\n' % ret
            if ret == 0:
                child.sendline('yes\n')
            elif ret == 1:
                child.sendline(pwd + '\n')
            elif ret == 2: # prompt
                break
            elif ret == 5: # No route to host
                return;
                
        #print 'run commands\n'
        # run commands
        result = True
        run_times = cfg.loop_count
        while True:
            cmd_index = 0
            for cmd in self.cmds:
                cmd_index += 1
                child.sendline(cmd)
                time.sleep(cfg.cmd_delay)
                ret = child.expect([self.prompt, EOF, TIMEOUT])
                if ret == 2:
                    result = False
                    if cfg.error_log:
                        common.savelog(self.getName(), child.before);
                    break

                if self.display:
                    print "\n%s" % ('*' * 40)
                    print "\nThread %s is running %s" % (self.getName(), cmd)
                temp_flow = len(cmd)
                if type(child.before) == types.StringType:
                    temp_flow += len(child.before)
                    if self.display: print child.before
                if type(child.after) == types.StringType:
                    temp_flow += len(child.after)
                    if self.display: print child.before
                self.flow += temp_flow
                self.ss.add(temp_flow);
                if self.display:
                    print "%s\n" % ('*' * 40)
                    self.display = False
                #print "*speed=%s(%d) add=%d" % (self.ss.speed_str(), self.ss.speed(), temp_flow)

                #if test_ssh.display:
                    #print "%d.%d>%s[%d]" % (run_times, cmd_index, cmd, self.flow)
            
            if cfg.loop_count > 0:
                run_times -= 1
                if run_times <= 0:
                    break;

            if not (result and test_ssh.running):
                break;
                
        child.close()
        if result:                
            test_ssh.success_count += 1
        else:
            test_ssh.failed_count += 1
        #if test_ssh.display:
            #print "%s" % ('*' * 40)
        print "* {%s}mission accomplish: total %d bytes, success=%d failed=%d" % (self.getName(), self.flow, test_ssh.success_count, test_ssh.failed_count)
            #print "%s" % ('*' * 40)
    def test_scp(self, cfg):
        child = None
        cmdline, pwd = cfg.scp, cfg.scp_pwd
        if test_ssh.display_all:
            child = spawn(cmdline, logfile=sys.stdout, timeout=60*2)
        else:
            child = spawn(cmdline, timeout=60*2)
        ret = 0
        while ret < 1:
            ret = child.expect(["yes/no", "password:", EOF, TIMEOUT])
            if ret == 0:
                child.sendline('yes\n')
            elif ret == 1:
                child.sendline(pwd + '\n')


def SignalHandler(sig, id):
    global display_detail
    global cmd_mode
    
    if sig == signal.SIGUSR1:
        display_detail = not display_detail
    elif sig == signal.SIGUSR2:
        cmd_mode = True

def register_signal():
    signal.signal(signal.SIGUSR1, SignalHandler)
    signal.signal(signal.SIGUSR2, SignalHandler)

def encode_str(str1):
    return base64.encodestring(str1)

def decode_str(str1):
    return base64.decodestring(str1)
    
def main():
    global display_detail
    global cmd_mode
    count = 0;
    
    register_signal()
    conf_file = AppSet.default_file
    
    for i in sys.argv[1:]:
        if i == '-d':  
            test_ssh.display_all = True
        elif i == '--help' or i == '-h':
            show_usage()
            sys.exit(0)
        elif i == 'scp':
            test_ssh.scp = True
        elif i == '-p':
            temp_str = encode_str(sys.argv[2])
            print "%s --> %s" % (temp_str, decode_str(temp_str))
            sys.exit(0)
        elif i == '-c':
            conf_file = sys.argv[2]
            
    cfg = AppSet.getInstance()
    cfg.load(conf_file)
    thread_count = cfg.thread_count
    
    print "starting..."
    #print "%s[No.] - success_rate - Connect Success | Connect Failed%s" % ('-' *10, '-' *10)
    
    thread_loop_count = cfg.thread_loop_count
    while(test_ssh.running):
        threads = []
        block_rate = 100
        total_count = test_ssh.success_count + test_ssh.failed_count
        if total_count > 0:
            block_rate = float(test_ssh.success_count) / float(total_count) * 100
        #print "%s%d| %d%% | %d | %d|%s" % ('-' *20, count, block_rate, test_ssh.success_count, test_ssh.failed_count, '-' *20)
        count  = count + 1
        for i in range(0, thread_count):
            thread = test_ssh(cfg)
            thread.setName("T" + str(i + 1))
            thread.start()
            threads.append(thread)
            time.sleep(cfg.get_thread_delay())

        print "working..."
        start_time = time.time()
        alive_count = thread_count
        die_count = 0

        ss = speed_statistics(1)
        while alive_count > 0:
            #for t in threads:
            #    t.join(timeout=1)
                
            alive_count = 0
            die_count = 0
            flow = 0
            index = 0
            temp_str = ''
            for t in threads:
                index += 1
                if t.isAlive(): 
                    if display_detail: temp_str += '%4d.[*] %s' % (index, t.ss.speed_str())
                    alive_count += 1
                else: 
                    if display_detail: temp_str += '%4d.[ ] %s' % (index, t.ss.speed_str())
                    die_count += 1
                if index % 3 == 0:
                    if display_detail: print temp_str
                    if display_detail: temp_str = ''
                else:
                    if display_detail: temp_str += '\t'
                flow += t.ss.speed()
            ss.update(flow)
            print "[+%d %s]thread alive=%d/%d total=%s speed=%s\n" % ((time.time() - start_time)/60, time.strftime('%Y%m%d %X', time.localtime(time.time())), alive_count, len(threads), common.get_flow_hs(flow), ss.speed_str())
            
            display_detail = False
            
            if cmd_mode:
                try:
                    tid = raw_input('Enter thread index: ')
                    tid = int(tid) - 1
                    if tid >= 0 and tid < len(threads):
                        threads[tid].display = True
                except:
                    pass
                cmd_mode = False
            time.sleep(120)
            
        
        if test_ssh.error_count > 0:
            print "error_count = %d\n" % test_ssh.error_count
            
        if cfg.thread_loop_count > 0:
            thread_loop_count -= 1
            if thread_loop_count <= 0:
                test_ssh.running = False
    print
    print "%s" % ('*' *60)
    print "total %d connections, success_rate %d%%" % (count * thread_count, block_rate)
    print "connect success %d times" % (test_ssh.success_count)
    print "connect failed %d times" % (test_ssh.failed_count)
    print "%s" % ('*' *60)
    
if __name__ == "__main__":
    main()
