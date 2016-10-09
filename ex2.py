#!/usr/bin/env python
# -*- coding: utf-8 -*-
li = [11, 22, 8, -5, 4, 10, 5, 15]

# for j in range(1, len(li)):
#     key = li[j]
#     i = j - 1
#     # 向前查找插入位置
#     while i >= 0 and li[i] > key:
#         li[i + 1] = li[i]
#         i = i - 1
#         li[i + 1] = key
# print(li)

for i in range(len(li)):
    #position  = i
    while i > 0 and li[i] < li[i-1]:# 右边小于左边相邻的值
         tmp = li[i]
         li[i] = li[i-1]
         li[i-1] = tmp
         i -= 1
print(li)