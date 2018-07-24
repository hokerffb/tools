Tools
=====

My best tools for working

Install:

```
sudo ./install.sh
```

# Command

## fdp

Format 'docker ps' output

## where

Look if the python moudle exist

usage:

```
$ where <python-moudle-name> 
```

## ref

帮助在grep的结果中高亮出指定的关键词


# Example

```
$ grep -rnE "\.get_all\(" *|ref 5 5 "get_all"
$ docker ps|fdp
$ where pygame
```

# csv2srt

做视频字幕的时候，可以首先用Excel进行编辑修改，然后通过这个工具快速的把csv转换成srt字幕格式
