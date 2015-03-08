#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print '%s : %d' % (letter, c[letter])
    