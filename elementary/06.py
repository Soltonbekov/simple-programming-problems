# -*- coding: utf-8 -*-

print "Please enter integer:"
n = int(raw_input())

print "Please enter computing type:"
print "1 - Product, 2 - Sum"

comp_type = raw_input()
result = 1

if comp_type == "1":
    for i in range(1,n):
        result *= i
    print result
elif comp_type == "2":
    print sum(range(1,n))
else:
    print "Please enter correct choice"
