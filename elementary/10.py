# -*- coding: utf-8 -*-

# /4 leap
# /100 not leap
# /400 leap

import datetime

y = datetime.date.today().year
n = 0


while n <= 20:
    y += 1
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        n = n + 1
        print y

# for i in range(y,y+21):
#     if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
#         print i
