#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import sys
import requests
from bs4 import BeautifulSoup


def http_get(url):
    headers = {
        'host': 'booksdl.org',
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


def webfile_list(nickname):
    html = http_get(url)

    soup = BeautifulSoup(html, "html.parser")
    for child in soup.find_all('a'):
        if child['href'] == '../':
            print "../ <Pass>"
        elif child.text[-1:] == '/':
            print child.text.encode('utf8'), "<Dir>"
        else:
            print child.text.encode('utf8'), "<File>" 


if __name__ == '__main__':
    sys.setdefaultencoding('utf8')
    url = "http://booksdl.org/comics0/_COMICS_MAGAZINES/"
    webfile_list(url)