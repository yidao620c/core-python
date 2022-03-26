#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 参数跟返回值注解
注解不做任何事情，不做任何限制和坚持。只是提供IDE工具元信息
"""


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """在max_len前面或后面的第一个空格处截断文本注解版本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()
