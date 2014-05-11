#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mport collections

d = collections.deque(xrange(10))
print 'Normale           :', d
d = collections.deque(xrange(10))
d.rotate(2)
print 'Rotazione destra  :', d
d = collections.deque(xrange(10))
d.rotate(-2)
print 'Rotazione sinistra :', d