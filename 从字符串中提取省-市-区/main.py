# -*- coding:utf-8 -*-

import cpca
import os

path = os.path.dirname(__file__)
file = path + "/地址字符串.txt"
location_str = []

with open(file, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().splitlines()
        if not line:
            break
        location_str.append(line[0])

# print(location_str)

df = cpca.transform(location_str, cut=False,pos_sensitive=True)

df.to_csv('省-市-区.csv', encoding="utf_8_sig")
