#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# coding=utf8
# Usage: python3 gbk2utf8.py src.txt dest.txt
import io, sys

input = io.open(sys.argv[1], encoding="gbk").read()
output = io.open(sys.argv[2], "w", encoding="utf-8")
output.write(input)