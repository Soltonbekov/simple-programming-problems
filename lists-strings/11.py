# -*- coding: utf-8 -*-

L1 = [1,3,5,7,9,11,13,15,17,19]
L2 = [0,2,4,6,8,10,12,14,16,18]


def combineSort(list1,list2):
    L = sorted(list1 + list2)
    return L

print combineSort(L1, L2)
