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
    from datetime import datetime
    now = datetime.now() # 获取当前datetime
    print(now)
    print(type(now))

    from datetime import datetime
    dt = datetime(2016, 2, 22, 12, 20, 22) # 用指定日期时间创建datetime
    print(dt)

    from datetime import datetime
    dt = datetime(2016, 2, 22, 12, 20, 22) # 用指定日期时间创建datetime
    print(dt.timestamp())  # 把datetime转换为timestamp

    t = 1456114822.0
    print(datetime.fromtimestamp(t)) # 本地时间
    print(datetime.utcfromtimestamp(t)) # UTC时间

    cday = datetime.strptime('2016-9-9 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)

    dt = datetime(2016, 2, 22, 12, 20, 22) # 用指定日期时间创建datetime
    print(dt.strftime('%a, %b %d %H:%M'))

    from datetime import datetime, timedelta
    dt = datetime(2016, 2, 22, 12, 20, 22) # 用指定日期时间创建datetime
    print(dt + timedelta(hours=10))
    print(dt - timedelta(days=1))
    print(dt + timedelta(days=2, hours=12))

    from datetime import datetime, timedelta, timezone
    tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
    dt = datetime(2016, 2, 22, 12, 20, 22) # 用指定日期时间创建datetime
    print(dt)
    dt = dt.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
    print(dt)

    # 拿到UTC时间，并强制设置时区为UTC+0:00:
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
    # astimezone()将转换时区为北京时间:
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
    # astimezone()将转换时区为东京时间:
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)
    # astimezone()将bj_dt转换时区为东京时间:
    tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt2)






