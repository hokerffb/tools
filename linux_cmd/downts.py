#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf8

import os


def ts2mp4():
    cmd = "ffmpeg -y -i merge.ts -c:v libx264 -c:a copy output.mp4"
    os.system(cmd)


def remerge():
    os.system("rm -rf merge.ts")
    i = 0
    while(1):
        i = i + 1
        tsname = str(i) + '.ts'
        if not os.path.isfile(tsname):
            break
        cmd = "cat " + tsname + ">>merge.ts"
        os.system(cmd)
    ts2mp4()
    print('Done.')


def genscript(url_list_file):
    tsname = ""
    w = open(url_list_file + '.sh', 'w')
    with open(url_list_file, 'r') as f:
        i = 0
        for line in f.readlines():
            url = line.strip()
            if url == "":
                continue
            i = i + 1
            w.write('wget ' + url + ' -O ' + str(i) + '.ts\n')
    w.close()
    print("Done.")


def down_m3u8(url):
    pos = url.rfind('/')
    m3u8 = url[pos + 1:]
    endpoint = url[:pos]
    os.system("wget %s -O %s" % (url, m3u8))
    os.system("cat %s|grep ts > tslist.tmp" % (m3u8))
    w = open('down.sh', 'w')
    with open('tslist.tmp', 'r') as f:
        i = 0
        for line in f.readlines():
            ts = line.strip()
            if ts == "":
                continue
            i = i + 1
            if ts[:4] == 'http':
                row = 'wget %s -O %d.ts\n' % (ts, i)
            else:
                row = 'wget %s/%s -O %d.ts\n' % (endpoint, ts, i)
            w.write(row)
    w.close()
    os.system('rm tslist.tmp;ls -l;')


def show_usage():
    print('Download all ts files in url_list_file and merge to mp4 file.\n')
    print('usage:\n\tdownts [option] <url_file_name>\n')
    print('option:\n')
    print('\t--remerge : remerge all ts files in current directory.\n')
    print('\t--script <url_file_name>: generate download bash script file.\n')
    print('\t--m3u8 <m3u8_url>: down m3u8 and generate down script.\n')
    print('\n\tdownts <url_file_name.m3u8>\n')


def main(url_list_file):
    tsname = ""
    os.system("rm -rf merge.ts")
    with open(url_list_file, 'r') as f:
        i = 0
        for line in f.readlines():
            url = line.strip()
            if url == "":
                continue
            i = i + 1
            tsname = str(i) + '.ts'
            cmd = 'wget "' + url + '" -O ' + tsname
            os.system(cmd)
            cmd = "cat " + tsname + ">>merge.ts"
            os.system(cmd)
    ts2mp4()
    print("Done.")


# downts --remerge
# downts --script <urllistfile>
# downts <urllistfile>
if __name__ == "__main__":
    if len(os.sys.argv) < 2:
        show_usage()
        os.sys.exit(0)
    if os.sys.argv[1] == '--script' or os.sys.argv[1] == '-s':
        if len(os.sys.argv) < 3:
            show_usage()
            os.sys.exit(0)
        genscript(os.sys.argv[2])
        os.sys.exit(0)
    elif os.sys.argv[1] == '--remerge' or os.sys.argv[1] == '-r':
        remerge()
        os.sys.exit(0)
    elif os.sys.argv[1] == '--m3u8':
        down_m3u8(os.sys.argv[2])
        os.sys.exit(0)
    elif os.sys.argv[1][-5:] == '.m3u8':
        down_m3u8(os.sys.argv[1])
        os.sys.exit(0)
    else:
        main(url_list_file=os.sys.argv[1])
