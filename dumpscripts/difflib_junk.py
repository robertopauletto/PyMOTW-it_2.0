#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from difflib import SequenceMatcher

A = " abcd"
B = "abcd abcd"

print 'A = "%s"' % A
print 'B = "%s"' % B

s = SequenceMatcher(None, A, B)
i, j, k = s.find_longest_match(0, 5, 0, 9)
print 'isjunk=None     :', (i, j, k), '"%s"' % A[i:i+k], '"%s"' % B[j:j+k]

s = SequenceMatcher(lambda x: x==" ", A, B)
i, j, k = s.find_longest_match(0, 5, 0, 9)
print 'isjunk=(x==" ") :', (i, j, k), '"%s"' % A[i:i+k], '"%s"' % B[j:j+k]