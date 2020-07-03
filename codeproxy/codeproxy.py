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
import traceback
import json
import zmq
import os
import commands

def on_message_recv(cmd, args):
    ret = None
    if cmd == 'shell':
        if 'script' in args:
            script = args['script']
            print script
            output = os.popen(script).readlines()
        ret = {"code": 0,
                "message":"success",
                "data": {"script":script, "output":json.dumps(output)}
                }
    elif cmd == 'call':
        script = "sh run.sh"
        if 'script' in args:
            script = args['script']
        print script
        os.system(script)
        ret = {"code": 0,
                "message":"success",
                "data": script
                }
    elif cmd == "cmd":
        if 'command' in args:
            command = args['command']
        print command
        (retval, output) = commands.getstatusoutput(command)
        ret = {"code": 0,
                "message":"success",
                "data": {"retval":retval, "output":output}
                }
    else:
        print '*' * 60
        print "recv:", cmd, args
        ret = {"code": -1,
                "message":"Unknown error.",
                "data": {}
                }

    print time.ctime()
    return ret

if __name__ == '__main__':
    cfg = dict({"host":"0.0.0.0", "port":"7777"})
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://%(host)s:%(port)s" % cfg)
    print "listen tcp://%(host)s:%(port)s" % cfg
    
    while True:
        try:
            msg_type, uuid, message = socket.recv_multipart()
            msg = json.loads(message)
        except Exception, e:
            print e
            socket.send_multipart(["error", "0", json.dumps({
                            "code": -1,
                            "message":"Invalid data.",
                            "data": {}
                            })])
            time.sleep(1)
            continue
        if not msg.has_key("method") or not msg.has_key("args"):
            socket.send_multipart([msg_type, uuid, json.dumps({
                            "code": -1,
                            "message":"Invalid method.",
                            "data": {}
                            })])
            continue

        cmd = msg["method"]
        args = msg["args"]
        
        ret = on_message_recv(cmd, args)
        socket.send_multipart([msg_type, uuid, json.dumps(ret)])
        
