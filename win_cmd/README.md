# 总览

* clear.bat：删除当前目录和子目录中的所有Windows图片预览文件Thumbs.db。
* du.ps1：查看当前目录所有文件的大小

# 运行环境

要运行du.ps1，需要首先以管理员运行PowerShell，并执行

```
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned
```

# 用法示例

```在PowerShell中运行
> .\du.ps1
Path: D:\projects\tools\
Ezviz2kml 85.0 MB
ssh-test-tool 20.4 KB
csdn2md 9.9 KB
codeproxy 7.1 KB
linux_cmd 4.0 KB
cloudtesting 3.3 KB
.idea 3.3 KB
wp2md 2.5 KB
down_webfiles 2.0 KB
win_cmd 1.8 KB
gdb_httpd 1.3 KB
AppleReviewCrawl 1.2 KB
config 0.6 KB
```