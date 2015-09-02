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

def main():
    col = []
    count = 0
    cols = ["CONTAINER ID", "IMAGE", "COMMAND", "CREATED", "STATUS", "PORTS", "NAMES"]
    cols_index = []
    while True:
        pipline = sys.stdin.readline()
        if pipline is None or len(pipline) == 0:
            break
        if count == 0:
            # parse column
            for i in range(0, len(cols)):
                cols_index.append(pipline.find(cols[i]))
        else:
            # parse output
            print "%d.%s" % (count, "-" * 60)
            for i in range(0, len(cols)):
                if i + 1 == len(cols):
                    print "%s: %s" % (cols[i], pipline[cols_index[i] : ])
                else:
                    print "%s: %s" % (cols[i], pipline[cols_index[i] : cols_index[i + 1]])
        count += 1
    

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print 'usage: docker ps|fdp'
        sys.exit(0)

    main()
