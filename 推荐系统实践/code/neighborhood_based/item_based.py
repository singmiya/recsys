#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

import math

from flask import json

from user_based import *

data_path = os.path.abspath('.') + '/data/'


def make_matrix(items, C, N):
    for i in items:
        if i not in N:
            N[i] = 1
        else:
            N[i] += 1
        if i not in C:
            C[i] = dict()
        for j in items:
            if i == j:
                continue
            if j not in C[i]:
                C[i][j] = 1
            else:
                C[i][j] += 1


def item_similarity(train):
    """计算物品相似度"""
    print '%s: %s' % ('计算物品相似度', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    st = time.time()
    # build inverse table for user_items
    user_items = {key: [d['item'] for d in datas] for key, datas in train.items() if len(datas) > 0}

    # calculate co-rated users between items
    C = dict()
    N = dict()
    for _, items in user_items.items():
        make_matrix(items, C, N)

    # calculate final similarity matrix W
    W = dict()
    for i, related_items in C.items():
        if i not in W:
            W[i] = dict()
        for j, cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j]) * 1.0

    print '计算物品相似度耗时，{%fs}' % (time.time() - st)

    st = time.time()
    file1 = open(data_path + 'item_similarity.txt', 'w')
    file1.write(json.dumps(W))
    file1.close()
    print '写入耗时，{%fs}' % (time.time() - st)


def recommend(user, train, W, top):
    """生成推荐列表"""
    rank = dict()
    related_items = train[user]
    for d in related_items:
        i, rui = d['item'], d['rating']
        topN = sorted(W[i].iteritems(), key=lambda d: d[1], reverse=True)[0:top]
        for j, wij in topN:
            if j in related_items:
                continue
            if j not in rank:
                rank[j] = wij * int(rui)
            else:
                rank[j] += wij * int(rui)
    return rank


def recommend_reasoned(user, train, W, top):
    """带有推荐理由的推荐"""
    rank = dict()
    related_items = train[user]
    for d in related_items:
        i, rui = d['item'], d['rating']
        topN = sorted(W[i].iteritems(), key=lambda d: d[1], reverse=True)[0:top]
        for j, wij in topN:
            if j in related_items:
                continue

            if j not in rank:
                rank[j] = dict()
                rank[j]['weight'] = wij * int(rui)
            else:
                rank[j]['weight'] += wij * int(rui)

            if 'reason' not in rank[j]:
                rank[j]['reason'] = dict()

            if i not in rank[j]['reason']:
                rank[j]['reason'][i] = wij * int(rui)
            else:
                rank[j]['reason'][i] += wij * int(rui)

    return rank


if __name__ == "__main__":
    """item based"""
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    path = os.path.abspath('.') + '/data/ml-100k/u.data'
    lines = []
    file = open(path)
    lines = file.readlines()
    file.close()
    data = []
    for line in lines:
        line = line.replace('\n', '')
        meta_data = dict()
        values = line.split('\t')
        # noinspection PyBroadException
        try:
            meta_data['user'] = values[0]
            meta_data['item'] = values[1]
            meta_data['rating'] = values[2]
            meta_data['timestamp'] = values[3]
            data.append(meta_data)
        except:
            continue

    train, test = split_data(data, 8, 1, 4)

    st = time.time()
    train1 = dict()
    for data1 in train:
        user = data1['user']
        if user not in train1:
            train1[user] = [data1]
        else:
            train1[user].append(data1)
    test1 = dict()
    for data1 in test:
        user = data1['user']
        if user not in test1:
            test1[user] = [data1]
        else:
            test1[user].append(data1)
    print '整理数据耗时，{%fs}' % (time.time() - st)

    file1 = open(data_path + 'item_similarity.txt')
    W = json.loads(file1.readlines()[0])
    file1.close()

    print recommend_reasoned('3', train1, W, 5)
    # item_similarity(train1)
    # recall(train1, test1, 5, 'item_similarity.txt', recommend)
    # precision(train1, test1, 5, 'item_similarity.txt', recommend)
    # coverate(train1, test1, 5, 'item_similarity.txt', recommend)
