# Linux Command

* ai：获取自动增加的数字，方便批量下载小电影使用；
* cax：16进制查看文件内容；
* csv2srt：做视频字幕的时候，可以首先用Excel进行编辑修改，然后通过这个工具快速的把csv转换成srt字幕格式
* downts：下载指定文件中的全部ts分片文件，并顺序编号后，合成一个mp4文件
* scan：扫描家庭网络中的设备IP地址
* fdp：格式化 'docker ps' 的输出
* where：查看指定的python模块是否存在
* ref：帮助在grep的结果中高亮出指定的关键词

同样适用于WSL和FreeBSD


# 用法示例

```
$ docker ps|fdp
$ where pygame
$ grep -rnE "\.get_all\(" *|ref 5 5 "get_all"
```

# 安装和卸载

Install: 
```
sudo make install
```

Uninstall:
```
sudo make uninstall
```