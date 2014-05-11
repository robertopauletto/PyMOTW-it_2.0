#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

def default_factory():
    return 'valore predefinito'

d = collections.defaultdict(default_factory, foo='bar')
print d
print d['foo']
print d['bar']