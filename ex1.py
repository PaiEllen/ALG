#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 冒泡排序
"""
li = [99,12,87,92]
temp = ""
for i in range(1,len(li)):
    for j in range(len(li) - 1):
        if li[j] > li[j +1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] =temp
print(li)
"""
#选择排序
'''

sma_index = 0
for j in range(1, len(li)):
    if li[j] < li[sma_index]:
        sma_index = j
temp = li[sma_index]
li[sma_index] = li[0]
li[0] = temp
'''
li = [11, 22, 8, -5]

for i in range(len(li)):
    sma_index = i
    for j in range(i,len(li)):
        if li[j] < li[sma_index]:
            sma_index = j
    temp = li[sma_index]
    li[sma_index] = li[i]
    li[i] = temp
print(li)