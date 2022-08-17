#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
#coding=utf8

"""
pip3 install Pillow
"""

import sys
from itertools import product
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

# mark color:005293/00569b/589e --> #005ba3
# 
OBJECT_MARK = (0, int('0x52',16), int('0x93',16))
OBJECT_BACK = (0, int('0x5b',16), int('0xa3',16), 255)
TOLERANCE = 15 # 容差

# 约等于
def approximate(a, b):
    if a > b - TOLERANCE and a < b + TOLERANCE:
        return True
    else:
        return False

def main(src, dest):
    img = Image.open(src)
    width, height = img.size
    change = False
    for pos in product(range(width), range(height)):
        pix = img.getpixel(pos)[:3]
        if pix == OBJECT_MARK:
            img.putpixel(pos, OBJECT_BACK)
            change = True
        if approximate(pix[1], OBJECT_MARK[1]) and approximate(pix[2], OBJECT_MARK[2]):
            # print(pix, XMIND_MARK, XMIND_BACK)
            img.putpixel(pos, OBJECT_BACK)
            change = True
    if change:
        img.save(dest)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('python3 rx.py src.png dest.png')
        sys.exit(0)
    src = sys.argv[1]
    dest = sys.argv[2]
    main(src, dest)
