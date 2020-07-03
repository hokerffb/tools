#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 Toyshop Studio
# All Rights Reserved.
# Author: YuWei Peng <pengyuwei@gmail.com>
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
import json
import zmq


def show_result(data):
    if 'data' in data:
        if 'script' in data['data']:
            print "$", data['data']['script']
        if 'output' in data['data']:
            try:
                output = json.loads(data['data']['output'])
                for i in output:
                    sys.stdout.write(i)
                    sys.stdout.flush()
            except:
                output = data['data']['output']
                print output
        if 'retval' in data['data']:
            print "return", data['data']['retval']
        return
    print data
    
def invoke(socket, param):
    socket.send_multipart (["client", "1", json.dumps(param)])

    #  Get the reply.
    msg_type, uuid, message = socket.recv_multipart()
    
    return json.loads(message)
    
    
def main():
    script = None
    cfg = dict({"host":"10.210.228.15", "port":"7777"})
    request = {
                "method": "",
                "args": {
                }
            }
    
    if len(sys.argv) == 2:
        script = sys.argv[1]
        request['method'] = "shell"
        request['args']['script'] = script
    elif len(sys.argv) == 1:
        request['method'] = "call"
        os.system("sh pre.sh")
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-c':
            command = sys.argv[2]
            request['method'] = "cmd"
            request['args']['command'] = command
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://%(host)s:%(port)s" % cfg)
    time.clock()

    data = invoke(socket, request)
    show_result(data)

    
if __name__ == '__main__':
    main()
