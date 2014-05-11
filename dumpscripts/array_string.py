#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import array
import binascii

s = 'Questo è un array.'
a = array.array('c', s)

print 'Come stringa:', s
print 'Come array :', a
print 'Come hex   :', binascii.hexlify(a)

