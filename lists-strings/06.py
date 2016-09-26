# -*- coding: utf-8 -*-

P = "put it up"


def isPalindrome(init_string):

    init_string = init_string.upper().replace(" ", "")
    j = len(init_string) - 1

    for i in init_string:
        if i == init_string[j]:
            True
        else:
            return False
        j -= 1
    return True

print isPalindrome(P)
