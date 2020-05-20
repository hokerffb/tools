#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import os
import csv

# srt format:
# 45
# 00:02:52,184 --> 00:02:53,617
# 慢慢来

# python ~/Documents/tools/csv2srt.py 课程内容
# input:  课程内容.csv
# output: 课程内容.srt

def main(src_file):
    dst_file = src_file + ".srt"
    src_file = src_file + ".csv"

    csvFileR = open(src_file, "r")
    reader = csv.reader(csvFileR)
    writer = open(dst_file, "w")

    i = 0
    for item in reader:
        i += 1
        start = int(item[0])
        keep = int(item[1])
        content = item[2]
        nick = ""
        if len(item) > 3:
            nick = item[3]

        m, s = divmod(start, 60)
        h, m = divmod(m, 60)
        strtime = "%d:%02d:%02d" % (h, m, s)
        strtime += ",000 --> "
        m, s = divmod(keep+start, 60)
        h, m = divmod(m, 60)
        strtime += "%d:%02d:%02d" % (h, m, s)
        strtime += ",000"

        print "%d %s %s" % (i, strtime, content)
        writer.write(str(i) + "\n")
        writer.write(strtime + "\n")
        if len(nick)==0 or nick == "——":
            writer.write("%s\n\n" % (content))
        else:
            writer.write("%s:%s\n\n" % (nick, content))

    writer.close()
    csvFileR.close()



if __name__ == "__main__":
    if len(os.sys.argv) < 2:
        print 'usage'
        os.sys.exit(0)
    main(src_file=os.sys.argv[1])