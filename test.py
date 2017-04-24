#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desc: something
"""
import collections
from collections import defaultdict
import fileinput
import itertools

pool_names_db = ['11', '22', '33', '44', '55']
pool_names_ceph = ['00', '11', '22']

to_deleted = set(pool_names_db) - set(pool_names_ceph)
to_added = set(pool_names_ceph) - set(pool_names_db)

print('pool_sync, deleted={}, added={}'.format(to_deleted, to_added))
