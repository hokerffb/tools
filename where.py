#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 Toyshop Studio
# All Rights Reserved.
# Author: Peng YuWei <pengyuwei@gmail.com>
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
import time
import os


def show_path(m):
    try:
        print __import__(m).__file__
    except:
        print "not found."

def main():
    if len(sys.argv) == 2:
        moudle = sys.argv[1]
        show_path(moudle)
    else:
        print "where <python-moudle name>"

if __name__ == '__main__':
    main()
