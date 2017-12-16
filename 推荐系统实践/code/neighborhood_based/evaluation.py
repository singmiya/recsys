#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import math
from flask import json
""" 评测指标：
    召回率
    准确率
    覆盖率
    流行度
"""

data_path = os.path.abspath('.') + '/data/'


def recall(train, test, N, filename, recommend):
    """召回率"""
    print "%s: %s" % ('recall', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    st = time.time()
    file1 = open(data_path + filename)
    W = json.loads(file1.readlines()[0])
    file1.close()

    hit = 0
    all = 0
    for user in train.keys():
        if user not in test:
            continue
        tu = [d['item'] for d in test[user]]
        rank = recommend(user, train, W, N)
        trainu = [d[0] for d in rank]
        hit += len(list(set(tu).intersection(set(trainu))))
        all += len(tu)

    print hit
    print all
    print hit / (all * 1.0)
    print '计算召回率耗时，{%fs}' % (time.time() - st)


def precision(train, test, N, filename, recommend):
    """准确率"""
    print "%s: %s" % ('precision', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    st = time.time()
    file1 = open(data_path + filename)
    W = json.loads(file1.readlines()[0])
    file1.close()
    hit = 0
    all = 0

    for user in train.keys():
        if user not in test:
            continue
        tu = [d['item'] for d in test[user]]
        rank = recommend(user, train, W, N)
        trainu = [d[0] for d in rank]
        hit += len(list(set(tu).intersection(set(trainu))))
        all += len(trainu)

    print hit
    print all
    print hit / (all * 1.0)
    print '计算精确率耗时，{%fs}' % (time.time() - st)


def coverate(train, test, N, filename, recommend):
    """覆盖率"""
    print "%s: %s" % ('coverate', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    st = time.time()
    # file1 = open(os.path.abspath('.') + '/data/123.txt')
    file1 = open(data_path + filename)
    W = json.loads(file1.readlines()[0])
    file1.close()
    hit = 0
    all = 0
    recommend_items = set()
    all_items = set()
    for user in train.keys():
        if user not in train:
            continue
        tu = [d['item'] for d in train[user]]
        rank = recommend(user, train, W, N)
        trainu = [d[0] for d in rank]
        recommend_items |= set(trainu)
        all_items |= set(tu)
    hit = len(recommend_items)
    all = len(all_items)
    print hit
    print all
    print hit / (all * 1.0)
    print '计算覆盖率耗时，{%fs}' % (time.time() - st)


def popularity(train, test, N, filename, recommend):
    """流行率"""
    print "%s: %s" % ('popularity', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    st = time.time()
    file1 = open(data_path + filename)
    W = json.loads(file1.readlines()[0])
    file1.close()
    item_popularity = dict()
    for user, datas in train.items():
        for d in datas:
            item = d['item']
            if item not in item_popularity:
                item_popularity[item] = 1
            else:
                item_popularity[item] += 1
    ret = 0
    n = 0
    for user in train.keys():
        rank = recommend(user, train, W, N)
        for item, pui in rank:
            ret += math.log(1 + item_popularity[item])
            n += 1
    ret /= n * 1.0
    print ret
    print '计算流行率耗时，{%fs}' % (time.time() - st)
