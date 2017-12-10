#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import math

from flask import json


def split_data(data, M, k, seed):
    train = []
    test = []
    random.seed(seed)
    for d in data:
        if random.randint(0, M) == k:
            test.append(d)
        else:
            train.append(d)
    return train, test


def user_similarity(train):
    # build inverse table for item_users
    item_users = dict()
    for data in train:
        user, item = data['user'], data['item']
        if item not in item_users:
            item_users[item] = set()
        item_users[item].add(user)

    item_users = {item: users for item, users in item_users.items() if len(item_users[user]) > 0}
    # calculate co-rated items between users
    C = dict()
    N = dict()
    for item, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 1
            else:
                N[u] += 1
            if u not in C:
                C[u] = dict()
            for v in users:
                if u == v:
                    continue
                if v not in C[u]:
                    C[u][v] = 1
                else:
                    C[u][v] += 1

    # calculate final similarity matrix W
    W = dict()
    for u, relate_users in C.items():
        if u not in W:
            W[u] = dict()
        for v, cuv in relate_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v]) * 1.0

    return W


def recommend(user, train, top):
    file1 = open(os.path.abspath('.') + '/data/123.txt')
    W = json.loads(file1.readlines()[0])
    file1.close()
    rank = dict()
    interacted_items = [item for item in train if item['user'] == user]

    for v, wuv in sorted(W[user].iteritems(), key=lambda d: d[1], reverse=True)[0:top]:
        for i, rvi in {item['item']: item['rating'] for item in train if item['user'] == v}.items():
            if i in interacted_items:
                # we should filter items user interacted before
                continue
            if i not in rank:
                rank[i] = wuv * float(rvi)
            else:
                rank[i] += wuv * float(rvi)
    return sorted(rank.iteritems(), key=lambda d: d[1], reverse=True)



def recall(train, test, N):
    '''召回率'''
    hit = 0
    all = 0
    for d in train:
        tu = {item['item']: item['rating'] for item in test if item['user'] == d['user']}
        rank = recommend(d['user'], train, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)
    return hit / (all * 1.0)


def precision(train, test, N):
    '''准确率'''
    hit = 0
    all = 0


def coverate(train, test, N):
    '''覆盖率'''
    hit = 0
    all = 0


if __name__ == "__main__":
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

    train, test = split_data(data, 5, 0, 4)
    # w = user_similarity(train)
    print recall(train, test, 10)
