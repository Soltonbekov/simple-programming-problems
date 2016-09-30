# -*- coding: utf-8 -*-

L = [1,2,3,4,5,6,7,8,9,10,]


def getSumLoop(init_list):
    j = 0
    for i in init_list:
        j += i
    return j


def getSumWhile(init_list):
    j = 0
    i = 0
    while i < len(init_list):
        j += init_list[i]
        i += 1
    return j


def getSumRecurs(init_list):
    if len(init_list) == 1:
        return init_list[0]
    else:
        return init_list[0] + getSumRecurs(init_list[1:])

print getSumLoop(L)

print getSumWhile(L)

print getSumRecurs(L)
