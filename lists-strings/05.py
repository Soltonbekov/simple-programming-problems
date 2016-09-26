# -*- coding: utf-8 -*-

#Write a function that computes the running total of a list.

L = [1,2,3,4,5,6,7,8,9,10,]

def returnRunningTotal(init_list):
    I = []
    F = []
    for i in init_list:
        I.append(i)
        F.append(sum(I))
    return F

print returnRunningTotal(L)
