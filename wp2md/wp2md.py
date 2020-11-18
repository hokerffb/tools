#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import sys
import requests
from bs4 import BeautifulSoup
import re


def http_get(url):
    headers = {
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


def get_blog_html(nickname, year, page):
    url = "https://%s.wordpress.com/%s/page/%d" % (nickname, year, page)
    return http_get(url)


def get_detail(obj):
    url = obj.find('a', rel=None)['href']
    html = http_get(url)
    soup = BeautifulSoup(html, "html.parser")
    ret = soup.find('div', class_='entry-content').text # bvMsg
    # title = soup.h1.string.encode('utf-8').strip()
    # article = soup.article.text.encode('utf-8').strip()
    return ret
    # create_time = ""
    # for child in soup.find_all('span', class_='time'):
    #     if len(child.text) == 19:
    #             create_time = child.text.strip()
    # return title, create_time, article


def blog_list(nickname, year):
    # https://hokerffb.wordpress.com/2007/page/2
    loop = True
    page = 0
    print 'Yearly Archives: %s年' % (year)
    print
    while (loop):
        page = page + 1
        html = get_blog_html(nickname, year, page)
        soup = BeautifulSoup(html, "html.parser")

        for child in soup.find_all(id=re.compile("post-\d+")):
            # <div id="post-134" class="post-134 post type-post status-publish format-standard hentry category-44049708">
            # if child.has_attr('id') and (child.id is not None) and 'post-' in child.id:
            
            # 标题，最末页没标题
            try:
                print "# " + child.h2.text
            except:
                loop = False
                break

            # Post on 2020/1/1 by 0xff
            print child.find('span', class_="meta-prep meta-prep-author").text \
                + ' ' + child.find('span', class_="entry-date").text \
                + ' by ' + child.find('a', class_="url fn n").text 
            print 
            
            # 正文
            if child.find('span', class_='meta-nav'):
                print get_detail(child)
            else:
                print child.p.text
            
            # 标签
            print 
            print child.find('span', class_="entry-utility-prep entry-utility-prep-cat-links").text \
                + ' ' \
                + child.find('a', rel="category tag").text
            print 
            print 


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'python wp2md.py nickname year'
        sys.exit(0)
    nickname = sys.argv[1]
    year = sys.argv[2]
    blog_list(nickname, year)
