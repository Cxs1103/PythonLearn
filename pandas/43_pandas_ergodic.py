#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 43_pandas_ergodic.py
@Date  : 2021/12/11 22:59
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas按行遍历DataFrame的3种方法
'''

import pandas as pd
import numpy as np
import collections
import timeit

df = pd.DataFrame(
    np.random.random(size=(100000, 4)),
    columns=list('ABCD')
)
print(df.head())
print(df.shape)

# 1. df.iterrows()
# 使用方式
for idx, row in df.iterrows():
    print(idx, row)
    print(idx, row["A"], row["B"], row["C"], row["D"])
    break

print("============================================")

s = '''
result = collections.defaultdict(int)
for idx, row in df.iterrows():
    result[(row["A"], row["B"])] += row["A"] + row["B"]
'''

# print(timeit.timeit(stmt=s,
#                     setup='import pandas as pd;'
#                           'import numpy as np;'
#                           'import collections;'
#                           'df = pd.DataFrame(np.random.random(size=(100000, 4)),columns=list("ABCD"))')
#       )

# 2. df.itertuples()
# 使用方式
for row in df.itertuples():
    print(row)
    print(row.Index, row.A, row.B, row.C, row.D)
    break

print("============================================")

# 3. for+zip
# 使用方式
# 既不需要类型检查，也不需要构建namedtuple
# 缺点是需要挨个指定变量
for A, B in zip(df["A"], df["B"]):
    print(A, B)
    break