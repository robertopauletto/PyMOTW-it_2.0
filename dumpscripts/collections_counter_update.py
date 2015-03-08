#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import collections

c = collections.Counter()
print 'Iniziale  :', c

c.update('abcdaab')
print 'Sequenza  :', c

c.update({'a':1, 'd':5})
print 'Dizionario:', c