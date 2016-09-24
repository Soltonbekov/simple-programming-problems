# -*- coding: utf-8 -*-

k=195 # secret number
n = 0
result = []

while n != k:
    n = int(input("Guess number: "))
    if n > k:
        result.append(n)
        print "Too large"
        print "Please try again"
    elif n < k:
        result.append(n)
        print "Too small"
        print "Please try again"
    elif n == k:
        result.append(n)
        print "Right!"

print result
