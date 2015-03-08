#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Più comuni:'
for letter, count in c.most_common(3):
    print '%s: %7d' % (letter, count)