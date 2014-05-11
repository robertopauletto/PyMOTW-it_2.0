#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

print 'Da destra  :'
d = collections.deque('abcdefg')
while True:
    try:
        print d.pop()
    except IndexError:
        break

print 'Da sinistra:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.popleft()
    except IndexError:
        break
