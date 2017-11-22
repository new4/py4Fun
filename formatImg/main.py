
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
别人给的切图尺寸不一致时，用这段代码将它们加工成相同尺寸
'''


import os
import math
from PIL import Image

CWD = os.getcwd()
SRC = os.path.join(CWD, 'src')
DIST = os.path.join(CWD, 'dist')

TARGET_WIDTH = 290
TARGET_HEIGHT = 208
TARGET_DATIO = TARGET_WIDTH / TARGET_HEIGHT


def resize_img(img):
    '''
    先按比例缩放图片，再切掉多出的部分
    '''
    ratio = img.width / img.height

    if ratio > TARGET_DATIO:
        # 太宽，以高度为准进行缩放
        target_width = math.floor(img.width * TARGET_HEIGHT / img.height)
        resized = img.resize((target_width, TARGET_HEIGHT), Image.LANCZOS)

        # 切掉左右两端
        padding_x = (target_width - TARGET_WIDTH) / 2
        cut = resized.crop((padding_x,
                            0,
                            resized.width - padding_x,
                            resized.height))
    else:
        # 太长，以宽度为准进行缩放
        target_height = math.floor(img.height * TARGET_WIDTH / img.width)
        resized = img.resize((TARGET_WIDTH, target_height), Image.LANCZOS)

        # 切掉上下两端
        padding_y = (target_height - TARGET_HEIGHT) / 2
        cut = resized.crop((0,
                            padding_y,
                            resized.width,
                            resized.height - padding_y))

    return cut


def run():
    '''
    运行函数
    '''
    mylist = os.listdir(SRC)
    for img_name in mylist:
        src = os.path.join(SRC, img_name)
        dist = os.path.join(DIST, img_name)
        with Image.open(src) as img:
            resize_img(img).save(dist, format='png')


if __name__ == '__main__':
    run()
