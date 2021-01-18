# ssh-test-tool

A multithreading performance test tool for ssh/scp

多线程的ssh性能测试工具，主要用于对ssh服务器的性能测试。

可以自动以指定线程数连接ssh服务器并执行设定的命令序列，

可以监控期间产生了多少流

```
python test_ssh.py
```

# conn_mysql.py

一个用于测试mysql数据库大量并发连接的python脚本，默认开启50个线程同时访问mysql数据库。
也可以适当修改实现其他测试功能。最初这个脚本是写来测试串行设备的。
运行环境：Linux/Windows

脚本在运行时可以通过
kill -s SIGUSR1 <pid>
来切换是否输出提示信息。


```
python conn_mysql.py
```