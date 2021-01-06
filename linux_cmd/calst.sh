#!/bin/bash
cd /var/log/nginx/
echo -n "deepview:";sudo grep "deepview" access.log|wc -l
echo -n "pro_thin:";sudo grep "pro_thin" access.log|wc -l
echo -n "basic_thin:";sudo grep "basic_thin" access.log|wc -l
echo -n "deepshot:";sudo grep "deepshot" access.log|wc -l
echo -n "test:";sudo grep "test" access.log|wc -l
echo "--------------------"
echo -n "total:";sudo grep "ics" access.log|wc -l
