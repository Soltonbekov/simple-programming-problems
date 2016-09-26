# -*- coding: utf-8 -*-

L = [9,8,7,6,5,4,3,2,1,]


def list_reverse(list_to_reverse):

    for i in range(0,list_to_reverse.__len__()):
        i = (list_to_reverse.__len__() - 1) - i
        list_to_reverse.insert(i,list_to_reverse.pop(0))

    print list_to_reverse

list_reverse(L)
