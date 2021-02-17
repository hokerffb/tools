# Overview

平时工作中会用到的一些工具性的代码


# List

* linux_cmd: Linux下的若干常用命令
* win_cmd: Windows下的若干常用命令
* config: 常用的配置文件
* AppleReviewCrawl: 苹果应用商店评论抓取工具
* csdn2md: CSDN博客抓取并转换为Markdown工具
* wp2md: WordPress博客按年抓取并转为Markdown文档
* csv2srt: csv格式文件转srt字幕格式
* ssh-test-tool: 多线程的ssh服务器性能测试工具
* [MySQL并发连接测试工具](ssh-test-tool/conn_mysql.py)
* ezviz2kml: 萤石云EZVIZ行车记录仪的轨迹txt文件转换为Google Earth可用的kml文件
* codeproxy: 代码分发工具
* down_webfiles: 从支持文件浏览的特定Web服务器上下载全部文件
* cloudtesting: PaaS平台测试工具
* gdb_httpd: PaaS平台httpd测试工具
* httpwatch: 运行于OpenWRT的http监控软件

# envirnment

```
sudo apt install -y git vim net-tools
sudo apt install -y build-essential
```

RTL8812BU-CG芯片的USB无线网卡驱动

```bash
sudo apt update
sudo apt -y install dkms git bc
git clone https://github.com/fastoe/RTL8812BU.git
cd RTL8812BU
VER=$(sed -n 's/\PACKAGE_VERSION="\(.*\)"/\1/p' dkms.conf)
sudo rsync -rvhP ./ /usr/src/rtl88x2bu-${VER}
sudo dkms add -m rtl88x2bu -v ${VER}
sudo dkms build -m rtl88x2bu -v ${VER}
sudo dkms install -m rtl88x2bu -v ${VER}
sudo modprobe 88x2bu
sudo reboot
```

确认显卡驱动
```
lspci|grep VGA
sudo lshw -c video
```


配置远程桌面
```
sudo apt install xrdp
sudo adduser xrdp ssl-cert
vi /etc/xrdp/startwm.sh
    注释：#test -x /etc/X11/Xsession && exec /etc/X11/Xsession
    注释：#exec /bin/sh /etc/X11/Xsession
    添加：gnome-session
    OS: enable Screen Sharing 
sudo service xrdp restart
netstat -an|grep tcp|grep 3389
sudo systemctl status xrdp
sudo systemctl status xrdp-sesman
```


