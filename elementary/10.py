# -*- coding: utf-8 -*-
years = 20

n = 10 #631 152 000 #secs in 20 years

import time

for i in xrange(1,n):
    time.sleep(1)
    print "%s seconds passed, %s seconds remain" % (i,n-i)
