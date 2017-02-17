#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desc: modify crushmap file by hand
"""
from collections import defaultdict
import fileinput
import re

def min_bucket_id(crush_file):
    min_id = 0
    id_pattern = re.compile(r'^\s*\bid\b\s+(-\d+)', re.MULTILINE)
    with open(crush_file) as f:
        content = f.read()
    for m in id_pattern.finditer(content):
        min_id = min(int(m.group(1)), min_id)
    return min_id


def max_rule_id(crush_file):
    max_id = 0
    id_pattern = re.compile(r'^\s*\bruleset\b\s+(\d+)', re.MULTILINE)
    with open(crush_file) as f:
        content = f.read()
    for m in id_pattern.finditer(content):
        max_id = max(int(m.group(1)), max_id)
    return max_id


def create_pool_byosd(pool_name, storage_policy, storage_type=0, hhd_osds=None, ssd_osds=None):
    """
    :param pool_name
        存储池名称
    :param storage_policy
        存储池策略
    :param storage_type
        存储池类型：(0:默认, 1:全HDD, 2:全SSD, 3:混合默认池, 4:混合主备池)
    :param hhd_osds
        hhd硬盘的osd，参数形式为[('1', 'node0001'), ('3', 'node0002')]
    :param ssd_osds
        ssd硬盘的osd，参数形式为[('0', 'node0002'), ('2', 'node0002')]
    :return:
    """
    # ...修改这个crushmap文件
    # 先找出最大id和最大ruleset
    crushfile_txt = 'd:/text.txt'
    min_bid = min_bucket_id(crushfile_txt)
    max_rid = max_rule_id(crushfile_txt)
    # 先主机分类
    hdd_dict = defaultdict(list)
    ssd_dict = defaultdict(list)
    if hhd_osds:
        for osdnum, hostname in hhd_osds:
            hdd_dict[hostname].append(osdnum)
    if ssd_osds:
        for osdnum, hostname in ssd_osds:
            ssd_dict[hostname].append(osdnum)
    root_start_pattern = re.compile(r'root default\s+')
    rule_start_pattern = re.compile(r'# rules\s+')
    end_start_pattern = re.compile(r'# end crush map\s+')
    find_root = False
    find_rule = False
    find_end = False
    if storage_type in [1, 2, 3]:
        all_hosts = []
        for line in fileinput.input(crushfile_txt, inplace=1):
            if not find_root and root_start_pattern.match(line.lstrip()):
                find_root = True
                for k, v in hdd_dict.items():
                    min_bid -= 1
                    all_hosts.append('winserver-{}-{}-hdd'.format(k, pool_name))
                    print('host winserver-{}-{}-hdd {{'.format(k, pool_name))
                    print('\tid {}		# do not change unnecessarily'.format(min_bid))
                    print('\t# weight 1.250')
                    print('\talg straw')
                    print('\thash 0	# rjenkins1')
                    for _osd in v:
                        print('\titem osd.{} weight 0.350'.format(_osd))
                    print('}')
                for k, v in ssd_dict.items():
                    min_bid -= 1
                    all_hosts.append('winserver-{}-{}-ssd'.format(k, pool_name))
                    print('host winserver-{}-{}-ssd {{'.format(k, pool_name))
                    print('\tid {}		# do not change unnecessarily'.format(min_bid))
                    print('\t# weight 1.250')
                    print('\talg straw')
                    print('\thash 0	# rjenkins1')
                    for _osd in v:
                        print('\titem osd.{} weight 0.350'.format(_osd))
                    print('}')
            if not find_rule and rule_start_pattern.match(line.lstrip()):
                find_rule = True
                min_bid -= 1
                print('root pool-{} {{'.format(pool_name))
                print('\tid {}		# do not change unnecessarily'.format(min_bid))
                print('\t# weight 0.700')
                print('\talg straw')
                print('\thash 0	# rjenkins1')
                for h in all_hosts:
                    print('\titem {} weight 0.350'.format(h))
                print('}')
            if not find_end and end_start_pattern.match(line.lstrip()):
                find_end = True
                max_rid += 1
                print('rule replicated_ruleset_{} {{'.format(pool_name))
                print('\truleset {}'.format(max_rid))
                print('\ttype replicated')
                print('\tmin_size 1')
                print('\tstep take pool-{}'.format(pool_name))
                print('\tstep chooseleaf firstn 0 type host')
                print('\tstep emit')
                print('}')
            print(line.rstrip())
    elif storage_type == 4:
        ssd_hosts = []
        hdd_hosts = []
        for line in fileinput.input(crushfile_txt, inplace=1):
            if not find_root and root_start_pattern.match(line.lstrip()):
                find_root = True
                for k, v in hdd_dict.items():
                    min_bid -= 1
                    hdd_hosts.append('winserver-{}-{}-hdd'.format(k, pool_name))
                    print('host winserver-{}-{}-hdd {{'.format(k, pool_name))
                    print('\tid {}		# do not change unnecessarily'.format(min_bid))
                    print('\t# weight 1.250')
                    print('\talg straw')
                    print('\thash 0	# rjenkins1')
                    for _osd in v:
                        print('\titem osd.{} weight 0.350'.format(_osd))
                    print('}')
                for k, v in ssd_dict.items():
                    min_bid -= 1
                    ssd_hosts.append('winserver-{}-{}-ssd'.format(k, pool_name))
                    print('host winserver-{}-{}-ssd {{'.format(k, pool_name))
                    print('\tid {}		# do not change unnecessarily'.format(min_bid))
                    print('\t# weight 1.250')
                    print('\talg straw')
                    print('\thash 0	# rjenkins1')
                    for _osd in v:
                        print('\titem osd.{} weight 0.350'.format(_osd))
                    print('}')
            if not find_rule and rule_start_pattern.match(line.lstrip()):
                find_rule = True
                min_bid -= 1
                print('root pool-{}-hdd {{'.format(pool_name))
                print('\tid {}		# do not change unnecessarily'.format(min_bid))
                print('\t# weight 0.700')
                print('\talg straw')
                print('\thash 0	# rjenkins1')
                for h in hdd_hosts:
                    print('\titem {} weight 0.350'.format(h))
                print('}')

                min_bid -= 1
                print('root pool-{}-ssd {{'.format(pool_name))
                print('\tid {}		# do not change unnecessarily'.format(min_bid))
                print('\t# weight 0.700')
                print('\talg straw')
                print('\thash 0	# rjenkins1')
                for h in ssd_hosts:
                    print('\titem {} weight 0.350'.format(h))
                print('}')

            if not find_end and end_start_pattern.match(line.lstrip()):
                find_end = True
                max_rid += 1
                print('rule rule-primary-{} {{'.format(pool_name))
                print('\truleset {}'.format(max_rid))
                print('\ttype replicated')
                print('\tmin_size 1')
                print('\tmax_size 10')
                print('\tstep take pool-{}-ssd'.format(pool_name))
                print('\tstep chooseleaf firstn 1 type host')
                print('\tstep emit')
                print('\tstep take pool-{}-hdd'.format(pool_name))
                print('\tstep chooseleaf firstn -1 type host')
                print('\tstep emit')
                print('}')
            print(line.rstrip())

# print(min_bucket_id('d:/text.txt'))
# print(max_rule_id('d:/text.txt'))

# hdd_osds = [('1', 'node0001'), ('3', 'node0001'), ('2', 'node0002')]
# ssd_osds = [('0', 'node0001'), ('4', 'node0001'), ('5', 'node0002')]
# create_pool_byosd('xiongneng', None, 4, hdd_osds, ssd_osds)

def merge_dict(base_dicts, update_dicts, key="name"):
    """
    merge dict by key based on base_dict
    :param base_dicts: base dict list
    :param update_dicts: update dict list
    :param key:
    :return:
    """
    for bdict in base_dicts:
        v = bdict[key]
        for udict in update_dicts:
            if udict[key] == v:
                bdict.update(udict)
                break
    return base_dicts

def remove_crushmap(crushfile_txt, pool_name):
    find_host = False
    find_root = False
    find_rule = False

    host_start_pattern = re.compile(r'host\s+.*-{}'.format(pool_name))
    root_start_pattern = re.compile(r'root\s+.*-{}'.format(pool_name))
    rule_start_pattern = re.compile(r'rule\s+.*-{}'.format(pool_name))

    for line in fileinput.input(crushfile_txt, inplace=1):
        if not find_host and host_start_pattern.match(line.lstrip()):
            find_host = True
        if not find_root and root_start_pattern.match(line.lstrip()):
            find_root = True
        if not find_rule and rule_start_pattern.match(line.lstrip()):
            find_rule = True
        if find_host and line.strip() == '}':
            find_host = False
            continue
        if find_root and line.strip() == '}':
            find_root = False
            continue
        if find_rule and line.strip() == '}':
            find_rule = False
            continue
        if find_host or find_root or find_rule:
            continue
        print(line.rstrip())

if __name__ == '__main__':
    """test"""
    remove_crushmap('d:/text.txt', 'xiongneng')


