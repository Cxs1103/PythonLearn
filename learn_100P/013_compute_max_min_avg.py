#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 013_compute_max_min_avg.py
@Date  : 2021/11/3 23:40
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''


def compute_score():
    scores = []
    with open('./datas/012_grade_file.txt') as fin:
        for line in fin:
            line = line[:-1]
            fields = line.split(",")
            scores.append(int(fields[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()

print(f'max_score={max_score}, min_score={min_score}, avg_score={avg_score}')
