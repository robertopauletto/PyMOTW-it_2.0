#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

for m in [ 1, 0, 0.1, 0.6 ]:
    print '%02.1f :' % m, datetime.time(0, 0, 0, microsecond=m)