# coding:utf8
import json

import jieba
seg_list=jieba.cut("我来到清华大学",cut_all=True)
print(seg_list)
for seg in seg_list:
    print(json.dumps(seg_list))
print(json.dumps(seg_list))