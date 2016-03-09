#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""
import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    """2015-12-12 12:12:12 UTC+5:00"""
    m = re.match('UTC([+-]\d+):(\d+)', tz_str)
    h = m.group(1)
    m = m.group(2)
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(
        tzinfo=timezone(timedelta(hours=int(h), minutes=int(m))))
    print(cday.timestamp())
    return cday.timestamp()


if __name__ == '__main__':
    t1 = to_timestamp('2015-06-01 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1


