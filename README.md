Overview
=====

平时工作中会用到的一些工具性的代码

Install:

```
sudo ./install.sh
```

# Tools

## AppleReviewCrawl

苹果应用商店评论抓取工具

```
arcgo <appid> > xxx.txt 
```

# Command

## fdp

格式化 'docker ps' 的输出

```
$ docker ps|fdp
```



## where

查看指定的python模块是否存在

usage:

``` 
$ where pygame
```

## ref

帮助在grep的结果中高亮出指定的关键词


```
$ grep -rnE "\.get_all\(" *|ref 5 5 "get_all"
```

# csv2srt

做视频字幕的时候，可以首先用Excel进行编辑修改，然后通过这个工具快速的把csv转换成srt字幕格式

# scan

扫描家庭网络中的设备IP地址
