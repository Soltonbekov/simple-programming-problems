# -*- coding: utf-8 -*-

print "Enter any integer:"

n = int(raw_input())

l = []

for i in range(1,n):
    if i%3 == 0 or i%5==0:
        l.append(i)

print sum(l)

