#!/bin/bash

for i in $(seq 2 255)
do
    ssh root@192.168.1.$i
done
