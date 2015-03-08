#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import collections

c = collections.Counter('estramamente')
c['z'] = 0
print c
print list(c.elements())    