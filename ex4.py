#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 希尔排序
import random
import time
#data_set = [ 11,22,9,-5,98,76,29,13,8,4,20,49,66,6,87]
data_set = [ random.randrange(i,10000) for i in range(1,10000)]
step = int(len(data_set)/2)
start_time = time.time()
while step >=1:
    for i in range(len(data_set) - step):
        if data_set[i] > data_set[i + step]:
            data_set[i], data_set[i + step] = data_set[i + step],data_set[i]
    step = int(step/2)
else:
    for i in range(len(data_set)):
        while i > 0 and data_set[i] < data_set[i-1]:
            tmp = data_set[i]
            data_set[i] = data_set[i - 1]
            data_set[i - 1] = tmp
            i -= 1

print("cost:", time.time() - start_time)
print(data_set)

