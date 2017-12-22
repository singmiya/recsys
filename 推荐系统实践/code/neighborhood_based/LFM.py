#!/usr/bin/python
# -*- coding: utf-8 -*-

"""隐语义模型 LFM"""
from user_based import *


def items_popularity(train):
    """生成物品流行度有序列表"""
    p_items = dict()
    for d in train:
        item, user = d['item'], d['user']
        if item not in p_items:
            p_items[item] = set()
        p_items[item].add(user)

    # 取流行度前500个物品
    top = 500
    p_items = sorted(p_items.items(), key=lambda d: len(d[1]), reverse=True)[0:top]
    return set([p_item[0] for p_item in p_items])


def user_items(train):
    """正样本  生成用户喜欢的物品的列表"""
    u_items = dict()
    for d in train:
        item, user = d['item'], d['user']
        if user not in u_items:
            u_items[user] = set()
        u_items[user].add(item)
    return u_items


def random_select_negative_simple(train):
    """负样本采样"""
    u_items = user_items(train)
    # 流行物品列表，即候选物品列表
    p_items = items_popularity(train)
    ret = dict()
    all_users = set([d['user'] for d in train])
    for user in all_users:
        # user 用户喜欢的物品的列表
        like = u_items[user]
        # 流行物品中user用户没有过行为的物品的列表
        if user not in ret:
            ret[user] = set()
        ret[user] = set(p_items).difference(set(like).intersection(p_items))
    return ret

if __name__ == "__main__":
    """LFM"""
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
    print random_select_negative_simple(train)