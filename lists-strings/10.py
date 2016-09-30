# -*- coding: utf-8 -*-

L1 = [1,2,3,4,5,6,7,8,9,10,]
L2 = [u"А",u"Б",u"В",u"Г",u"Д",u"Е",u"Ё",u"Ж",u"З",u"И",]


def listCombine(list1, list2):
    alter_list = []
    for i in xrange(len(list1)):
        alter_list.append(list1[i])
        alter_list.append(list2[i])
        i += 1
    return alter_list

print listCombine(L1, L2)
