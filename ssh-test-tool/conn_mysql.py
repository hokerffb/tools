#!/usr/bin/python
# by pyw[peng_yuwei@venus.com] 2010-10-27
# 一个用于测试mysql数据库大量并发连接的python脚本，默认开启50个线程同时访问mysql数据库。
# 也可以适当修改实现其他测试功能。最初这个脚本是写来测试串行设备的。
# 运行环境：Linux/Windows

# 脚本在运行时可以通过
# kill -s SIGUSR1 <pid>
# 来切换是否输出提示信息。

from pexpect import *
from threading import *
import sys
import signal

running = True

class conn_mysql(Thread):
	display = False
	success_count = 0;
	failed_count = 0;
	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
		Thread.__init__(self, group, target, name, args, kwargs, verbose)
	def run(self):
		self.test_case()
	def test_case(self):
		pwd = 'mysql -h192.168.11.182 -uroot -pcyberaudit'
		#child = spawn(pwd, logfile=sys.stdout)
		child = spawn(pwd)
		i = 0
		i = child.expect([r'mysql\>', 'ERROR', EOF, TIMEOUT])
		if i == 0:
			if conn_mysql.display:
				print "%s%s" % (child.before, child.after)
			child.sendline('show databases;')
			i = child.expect([r'mysql\>', 'ERROR', EOF, TIMEOUT])
			if i == 0:
				child.sendline('use mysql;')
				i = child.expect([r'mysql\>', 'ERROR', EOF, TIMEOUT])
				if i == 0:
					child.sendline('select * from user;')
					print "SQL success"
			conn_mysql.success_count += 1
			if conn_mysql.display:
				print "%s" % ('*' * 40)
				print "* login success, success_count=%d failed_count=%d" % (conn_mysql.success_count, conn_mysql.failed_count)
				print "%s" % ('*' * 40)
			child.sendline('exit')
		else:
			conn_mysql.failed_count += 1
		child.close()
		return

def SignalHandler(sig, id):
	global running
	if sig == signal.SIGUSR1:
		conn_mysql.display = not conn_mysql.display
	elif sig == signal.SIGINT:
		running = False
	elif sig == signal.SIGHUP:
		running = False
	elif sig == signal.SIGTERM:
		running = False
      
def register_signal():
	signal.signal(signal.SIGUSR1, SignalHandler)
	signal.signal(signal.SIGHUP, SignalHandler)
	signal.signal(signal.SIGTERM, SignalHandler)	
	signal.signal(signal.SIGINT, SignalHandler)
		
if __name__ == "__main__":
	register_signal()
	count = 0;
	thread_count = 1
	print "working..."
	print "%s[No.] - block_rate - Connect Success |  Connect Failed%s" % ('-' *10, '-' *10)
	while(running):
		threads = []
		block_rate = 100
		total_count = conn_mysql.success_count + conn_mysql.failed_count
		if total_count > 0:
			block_rate = float(conn_mysql.failed_count) / float(total_count) * 100
		print "%s%d| %d%% | %d | %d|%s" % ('-' *20, count, block_rate, conn_mysql.success_count, conn_mysql.failed_count, '-' *20)
		count  = count + 1
		for i in range(0, thread_count):
			thread = conn_mysql()
			thread.start()
			threads.append(thread)
		for t in threads:
			t.join()
	print
	print "%s" % ('*' *60)
	print "total %d connections, block_rate %d%%" % (count * thread_count, block_rate)
	print "connect success %d times" % (conn_mysql.success_count)
	print "connect failed %d times" % (conn_mysql.failed_count)
	print "%s" % ('*' *60)
				
			
