#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

l1=[11,22,33,44,55,66,77,88,99]

#rs={k1:[11,22,33,44,55],k2:[66,77,88,99]}
res_dict={}

for item in l1:
    if item < 66:
        if 'k1' in res_dict.keys():
            res_dict['k1'].append(item)
        else:
            res_dict['k1'] = []
    else:
        if 'k2' in res_dict.keys():
            res_dict['k2'].append(item)
        else:
            res_dict['k2'] = []




for k,v in res_dict.items():
    print k,v



