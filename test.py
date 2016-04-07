#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-06 03:08:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os, sys
import math


def fahrenheit_converter(c):
    print(str(c * 9 / 5 + 32) + '℉')


fahrenheit_converter(52)


def g2kg(g):
    g_value = int(g[:-1]) / 1000
    return g_value


kg = g2kg("50g")
print(kg)


def gougu(a, b):
    c = math.sqrt(a * a + b * b)
    return c


c = gougu(3, 4)
print("斜边长为为：" + str(c))

# 获取当前文件路径
print(sys.path[0])
# 获取当前真实路径
print(os.path.split(os.path.realpath(__file__))[0])

os.system("pause")
