#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import os


def comfirm_data(data, user1, user2):
    item1 = [d['item'] for d in data if d['user'] == user1]
    item2 = [d['item'] for d in data if d['user'] == user2]
    intersection = list(set(item1).intersection(set(item2)))
    print len(intersection)


if __name__ == "__main__":
    print "test"
    # path = os.path.abspath('.') + '/data/ml-100k/u.data'
    # lines = []
    # file = open(path)
    # lines = file.readlines()
    # file.close()
    # data = []
    # for line in lines:
    #     line = line.replace('\n', '')
    #     meta_data = dict()
    #     values = line.split('\t')
    #     # noinspection PyBroadException
    #     try:
    #         meta_data['user'] = values[0]
    #         meta_data['item'] = values[1]
    #         meta_data['rating'] = values[2]
    #         meta_data['timestamp'] = values[3]
    #         data.append(meta_data)
    #     except:
    #         continue
    # comfirm_data(data, '1', '199')
    # comfirm_data(data, '1', '452')
    # comfirm_data(data, '100', '199')
    cores = multiprocessing.cpu_count()
    print cores