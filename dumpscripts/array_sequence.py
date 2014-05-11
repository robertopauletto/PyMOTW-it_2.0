#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import array

a = array.array('i', xrange(5))
print 'Iniziale :', a

a.extend(xrange(5))
print 'Esteso   :', a

print 'Slice    :', a[3:6]

print 'Iteratore:', list(enumerate(a))

