# -*- coding: utf-8 -*-

L = [9,8,7,6,5,4,3,2,1,]


def checkList(list_for_check, element_for_check):
    return list_for_check.__contains__(element_for_check)

print checkList(L, "A")

print checkList(L, 1)
