#!/usr/bin/bash
ps aux --sort=-rss|head -20|awk '{if(NR>1) printf ("%.2fMB %s %d\n",$6/1024,$11, $2)}'
free -m
