#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bisect
import random

# Usa un seed costante per assicurarsi che si vedano 
# gli stessi numeri pseudo-casuali ogni volta che eseguiamo
# il ciclo.
random.seed(1)

# Genera 20 numeri casuali e
# li inserisce in una lista secondo un
# ordinamento
l = []
for i in range(1, 20):
	r = random.randint(1, 100)
	position = bisect.bisect(l, r)
	bisect.insort(l, r)
	print '%2d %2d' % (r, position), l
