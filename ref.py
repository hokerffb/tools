#!/usr/bin/python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 Toyshop Studio
# All Rights Reserved.
# Author: YuWei Peng <pengyuwei@gmail.com> 2012-3-23
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys
import linecache

OLOR_RED = "\033[1;31m"
COLOR_NONE = "\033[0m"
COLOR_RED = "\033[0;31m"
COLOR_GREEN = "\033[0;32m"
COLOR_BLUE = "\033[0;34m"
COLOR_YELLOW = "\033[1;33m"
COLOR_LIGHT_GREEN = "\033[1;32m"
COLOR_LIGHT_GRAY = "\033[0;37m"
COLOR_DARK_GRAY = "\033[1;30m"


def hlkey(string, key=None):
    #ret = string.replace(".", COLOR_LIGHT_GRAY + "." + COLOR_NONE)
    if not key is None:
        ret = string.replace(key, COLOR_RED + key + COLOR_NONE)
    else:
        ret = COLOR_RED + string + COLOR_NONE
    return ret


def main():
    pre = 0
    after = 2
    key = None
    if len(sys.argv) > 1:
        pre = int(sys.argv[1])
    if len(sys.argv) > 2:
        after = int(sys.argv[2])
    if len(sys.argv) > 3:
        key = sys.argv[3]
    count = 0
    while True:
        pipline = sys.stdin.readline()
        if pipline is None or len(pipline) == 0:
            break
        print
        #print pipline
        if not ":" in pipline:
            continue
        count += 1
        s = pipline.split(":")
        filename = s[0]
        line = int(s[1])
        print "%d. \033[1;32m%s\033[1;0m:%s%s\033[1;0m" % (count, filename, COLOR_RED, line)

        for i in range(1, pre + 1):
            sys.stdout.write(linecache.getline(filename, line - i))

        keyline = linecache.getline(filename, line)
        keyline = hlkey(keyline, key)
        sys.stdout.write(keyline)

        for i in range(1, after + 1):
            sys.stdout.write(linecache.getline(filename, line + i))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'usage: grep -rne "string" *|ref [pre] [after] [highlightkey]'
        sys.exit(0)

    main()
