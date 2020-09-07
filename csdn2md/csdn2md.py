#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import sys
import requests
from bs4 import BeautifulSoup


def http_get(url):
    headers = {
        'host': 'blog.csdn.net',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://www.greatwallheritage.cn',
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


def get_blog_list(nickname, page):
    url = "https://blog.csdn.net/%s/article/list/%d" % (nickname, page)
    return http_get(url)


def get_detail(url):
    html = http_get(url)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.h1.string.encode('utf-8').strip()
    article = soup.article.text.encode('utf-8').strip()
    create_time = ""
    for child in soup.find_all('span', class_='time'):
        if len(child.text) == 19:
                create_time = child.text.strip()
    return title, create_time, article


def blog_list(nickname):
    # https://blog.csdn.net/nickname/article/list/1
    page = 0
    while (True):
        page = page + 1
        html = get_blog_list(nickname, page)

        soup = BeautifulSoup(html, "html.parser")
        for child in soup.find_all('div'):
            # <div class="article-item-box csdn-tracking-statistics" data-articleid="84575961">
            if child.has_attr('data-articleid'):
                url = "https://blog.csdn.net/ffb/article/details/" + child['data-articleid']
                title, create_time, blog = get_detail(url)
                print "# " + title
                print "\n" + create_time + "\n"
                print "```"
                print blog
                print "```"
                print 

        # TODO: how to break?

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'python dump_csdn.py nickname'
        sys.exit(0)
    nickname = sys.argv[1]
    blog_list(nickname)
