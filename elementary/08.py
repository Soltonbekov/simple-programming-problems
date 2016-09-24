# -*- coding: utf-8 -*-

import sys

n = 10000

prime_list =[]

for i in xrange(2,n+1):
    for j in xrange(2,i):
        if i % j == 0:
            break
    else:
        prime_list.append(i)
print prime_list
