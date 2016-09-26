# -*- coding: utf-8 -*-

L = ["A","B","C","D","E","F","G",]

def returnOdd(init_list):
    for i in range(0, len(init_list)):
        if i%2 == 0:
            print init_list[i]

returnOdd(L)
