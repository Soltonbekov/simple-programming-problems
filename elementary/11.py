# -*- coding: utf-8 -*-

n = 10**6

for k in range(1, n+1):
    result = (-1) ** k / 2 * k - 1
    result += result

result = 4 * result

print result
