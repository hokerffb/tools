#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import os

def main(url_list_file):
    tsname = ""
    os.system("rm -rf merge.ts")
    with open(url_list_file, 'r') as f:
        i = 0
        for line in f.readlines():
            url = line.strip()
            if url == "":continue
            i = i + 1
            tsname = str(i) + '.ts'
            cmd = 'wget "' + url + '" -O ' + tsname
            os.system(cmd);
            cmd = "cat " + tsname + ">>merge.ts"
            os.system(cmd);
    cmd = "ffmpeg -y -i merge.ts -c:v libx264 -c:a copy output.mp4"
    os.system(cmd)
    print "Done."

if __name__ == "__main__":
    if len(os.sys.argv) < 2:
        print 'usage:\n\tdownts <url_file_name>\n'
        os.sys.exit(0)
    main(url_list_file=os.sys.argv[1])