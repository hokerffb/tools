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
import re

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
    col = []
    count = 0
    while True:
        pipline = sys.stdin.readline()
        if pipline is None or len(pipline) == 0:
            break
        print
        s = re.split('\t|  |   |    |     |      |        ', pipline)
        s1 = [item for item in s if item] 
        if count == 0:
            col = s1
        else:
            i = 0
            print s1
            for iter in s1:
                print "%d. %s: %s" % (i+1, col[i], s1[i])
                i += 1
        count += 1
    

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print 'usage: docker ps|fdp'
        sys.exit(0)

    main()
