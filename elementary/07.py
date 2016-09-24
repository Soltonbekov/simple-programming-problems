# -*- coding: utf-8 -*-

j = 1

for i in range(1, 13):
    n = j * i
    for k in range(1, 13):
        print "%s * %s = %s" % (n , k, n * k)
