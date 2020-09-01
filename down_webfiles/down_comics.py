#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import sys
import os
import requests
from bs4 import BeautifulSoup


def http_get(url):
    headers = {
        'host': 'XXX.org',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    return r.content


def webfile_list(url, downdir):
    html = http_get(url)

    soup = BeautifulSoup(html, "html.parser")
    for child in soup.find_all('a'):
        if child['href'] == '../':
            #print "../ <Pass>"
            pass
        elif child.text[-1:] == '/':
            #print child['href'], "<Dir>"
            # 递归
            #os.system('mkdir -p ' + downdir + child['href'])
            webfile_list(url + child['href'], downdir + child['href'])
        else:
            print url + child['href']
            # 下面代码因为涉及文件名中的特殊字符和目录转换问题，
            # 不如直接用下载工具下载上面打印出来的链接更省事
            #print child.text.encode('utf8'), "<File>" 
            # 下载文件
            #cmd = 'wget ' + url + child['href'] + ' -O "' + downdir + child.text + '"'
            #print cmd
            #os.system(cmd)


if __name__ == '__main__':
    url = "http://XXX.XXX/comics0/_COMICS_MAGAZINES/"
    webfile_list(url, 'down/')