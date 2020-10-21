#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
分位时
@Author: wanglanwei
@Date: 2020-09-24
@Time: 00:35:25
@Email: the.matrix.vvv@gmail.com or luckydreamcatcher@163.com
'''

import os
import sys


def percentile(simples, p):
    '''
    计算分位时
    Args:
        simples: 样本数组
        p: 百分比
    Returns:
        分位数
    '''
    if not simples or not p:
        return 0.0
    simples.sort()
    n = len(simples)
    rank = n*p - 1
    i = int(rank)
    j = rank - i
    return simples[i] + (simples[i+1] - simples[i]) * j


def read_data(f):
    '''
    从文件f中读取输入
    Args:
        f: 输入，包括标准输入、文件、网络等等
    Returns:
        样本数组
    '''
    res = []
    while True:
        num = f.readline().strip('\n')
        if not num or num == 'EOF':
            break
        res.append(float(num))
    return res



if __name__ == '__main__':
    # 读取百分比p
    p = 90
    if len(sys.argv) > 1:
        p = int(sys.argv[1])
    p = float(p) / 100
    # 从标准输出读取样本
    simples = read_data(sys.stdin)
    result = percentile(simples, p)
    print "percentile<%.2f>: %.2f" % (p, result)
