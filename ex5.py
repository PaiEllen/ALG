#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 最LOW堆排序
import random
import time
data_set = [ random.randrange(i,10000) for i in range(1,10000)]
start_time = time.time()
for j in range(len(data_set),1,-1):
    for i in range(int(j/2 - 1),-1,-1):
        left_child_index = i*2 + 1
        right_child_index = left_child_index + 1
        left_child = data_set[left_child_index]
        if left_child > data_set[i]:
            data_set[left_child_index],data_set[i] = data_set[i],data_set[left_child_index]
        if right_child_index < j:
            right_child = data_set[right_child_index]
            if right_child > data_set[i]:
                data_set[right_child_index],data_set[i] = data_set[i],data_set[right_child_index]

    data_set[0],data_set[j -1] = data_set[j - 1],data_set[0]
print("cost:", time.time() - start_time)
print(data_set)



