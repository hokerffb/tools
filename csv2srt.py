#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import os
import csv

# srt format:
# 45
# 00:02:52,184 --> 00:02:53,617
# 慢慢来

def main(src_file):
    dst_file = src_file + ".srt"

    csvFileR = open(src_file, "r")
    reader = csv.reader(csvFileR)
    writer = open(dst_file, "w")

    i = 0
    for item in reader:
        i += 1
        start = int(item[0])
        keep = int(item[1])
        content = item[2]

        m, s = divmod(start, 60)
        h, m = divmod(m, 60)
        print("%d:%02d:%02d" % (h, m, s))
        strtime = "%d:%02d:%02d" % (h, m, s)
        strtime += ",000 --> "
        m, s = divmod(keep+start, 60)
        h, m = divmod(m, 60)
        strtime += "%d:%02d:%02d" % (h, m, s)
        strtime += ",000"

        writer.write(str(i) + "\n")
        writer.write(strtime + "\n")
        writer.write(content + "\n\n")

    writer.close()
    csvFileR.close()



if __name__ == "__main__":
    if len(os.sys.argv) < 2:
        print 'usage'
        os.sys.exit(0)
    main(src_file=os.sys.argv[1])