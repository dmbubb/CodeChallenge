#!/usr/bin/env python3

import os
import sys
from collections import Counter




def rand_nums(howmany,startnum,endnum):
    myarr=[]
    for _ in range(howmany):
        myarr.append(randint(startnum, endnum))
    return myarr

def find_med(arr):
    if len(arr) %2 == 0:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
    if len(arr) %2 != 0:
        return arr[len(arr)//2 - 1]

def find_mode(myarr):
    myset=set(myarr)
    if len(myset) == len(myarr):
        return min(myarr)
    else:
        mydict={}
        max_count=0
        for i in myset:
            mydict[i] = myarr.count(i)
        max_val = max(sorted(set(mydict.values())))
        maxlist=[]
        for num, occur in mydict.items():
            if occur == max_val:
              maxlist.append(num)
        return min(maxlist)

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()

mean = sum(arr)/len(arr)

median = find_med(arr)

mode = find_mode(arr)
#mode = Counter(arr).most_common()[0][0]

print('{0:.1f}'.format(mean))
print('{0:.1f}'.format(median))
print('{0:.1f}'.format(mode))
