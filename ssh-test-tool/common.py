#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8
# create by 0xFF[pengyuwei@gmail.com] 2010-12-27
"""
the common function library class.
update by 0xFF[pengyuwei@gmail.com] 2010-12-29
"""

import unittest
import time

class common():
    def get_flow_hs(count):
        if count > 1048510:
            return "%.02fMB" % (count/1048510.0)
        elif count > 1024:
            return "%.02fKB" % (count/1024.0)
        else:
            return "%dByte" % (count)
    get_flow_hs = staticmethod(get_flow_hs)
    
    def savelog(filename, log):
        try:
            f = open(filename,'a')
            f.wirite(log)
            f.close()
        except:
            pass
    savelog = staticmethod(savelog)
            
class speed_statistics():
    """A easy speed statistics class"""
    def __init__(self, cyc):
        """cyc is compute(minutes)"""
        self.cyc = cyc*60
        self.last_time = time.time()
        self.count = 0
        self.last_count = 0
    def update(self, count=1):
        "data change to count"
        if (time.time() > self.last_time + self.cyc):
            self.last_count = self.count
            self.last_time = time.time()
            self.count = 0
        if self.count < count:
            self.count += count - self.count
    def add(self, count=1):
        "data add count"
        if (time.time() > self.last_time + self.cyc):
            self.last_count = self.count
            self.count = 0
            self.last_time = time.time()
        self.count += count
    def speed_str(self):
        return "%s/m" % (common.get_flow_hs(self.last_count))
    def speed(self):
        return self.last_count

class AppSetTest(unittest.TestCase):
    def test_speed_statistics(self):
        ss = speed_statistics(0.2)
        ss.add(3)
        time.sleep(30)
        ss.add(5)
        self.failIf(0 == ss.speed())
        print 'test_speed_statistics \t\t\t[OK]'
        
def test_case():
    import random
    sss = []
    for i in range(0,10):
        ss = speed_statistics(0.2)
        sss.append(ss)
    for i in range(0,100):
        flow = 0
        for ss in sss:
            ss.update(random.randint(1,50))
            flow += ss.speed()
            print "%s" % ss.speed_str()
            time.sleep(random.randint(0,1))
        print "total speed=%d/m" % (flow)
        time.sleep(2)
    print 'test_speed_statistics \t\t\t[OK]'

if __name__ == '__main__':
    test_case()
    #unittest.main()
