#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import os
import random
import math

import time
from flask import json
import thread

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

    # calculate final similarity matrix W  余弦相似度
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
    interacted_items = [d['item'] for d in train[user]]

    related_users = sorted(W[user].iteritems(), key=lambda d: d[1], reverse=True)[0:top]
    for v, wuv in related_users:
        for ui in train[v]:
            i, rvi = ui['item'], ui['rating']
            if i in interacted_items:
                # we should filter items user interacted before
                continue
            if i not in rank:
                rank[i] = wuv * float(1)
            else:
                rank[i] += wuv * float(1)
    rank = sorted(rank.iteritems(), key=lambda d: d[1], reverse=True)

    return rank


def recall(train, test, N):
    '''召回率'''
    print "%s: %s" % ('recall', time.ctime(time.time()))
    hit = 0
    all = 0
    for user in train.keys():
        if user not in test:
            continue
        tu = [d['item'] for d in test[user]]
        rank = recommend(user, train, N)
        trainu = [d[0] for d in rank]
        hit += len(list(set(tu).intersection(set(trainu))))
        all += len(tu)

    print hit
    print all
    print hit / (all * 1.0)


def precision(train, test, N):
    '''准确率'''
    print "%s: %s" % ('precision', time.ctime(time.time()))
    hit = 0
    all = 0
    for user in train.keys():
        if user not in test:
            continue
        tu = [d['item'] for d in test[user]]
        rank = recommend(user, train, N)
        trainu = [d[0] for d in rank]
        hit += len(list(set(tu).intersection(set(trainu))))
        all += len(trainu)

    print hit
    print all
    print hit / (all * 1.0)


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

    train, test = split_data(data, 8, 1, 4)
    # w = user_similarity(train)
    # file1 = open(os.path.abspath('.') + '/data/123.txt', 'w')
    # file1.write(json.dumps(w))
    # file1.close()
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

    try:
        thread.start_new_thread(recall, (train1, test1, 10))
        thread.start_new_thread(precision, (train1, test1, 10))
    except:
        print "Error: unable to start thread"