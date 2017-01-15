#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

from jinja2 import Template

template = Template('Hello {{ name }}')
print(template.render(name='John Doe'))
