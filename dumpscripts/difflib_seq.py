#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import difflib
from difflib_data import *

s1 = [ 1, 2, 3, 5, 6, 4 ]
s2 = [ 2, 3, 5, 4, 6, 1 ]

matcher = difflib.SequenceMatcher(None, s1, s2)
for tag, i1, i2, j1, j2 in matcher.get_opcodes(): 
    print ("%7s s1[%d:%d] (%s) s2[%d:%d] (%s)" % 
           (tag, i1, i2, s1[i1:i2], j1, j2, s2[j1:j2])) 