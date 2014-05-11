#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bisect
import random

# Reimposta il seed
random.seed(1)

# Usa bisect_left ed insort_left.
l = []
for i in range(1, 20):
	r = random.randint(1, 100)
	position = bisect.bisect_left(l, r)
	bisect.insort_left(l, r)
	print '%2d %2d' % (r, position), l
