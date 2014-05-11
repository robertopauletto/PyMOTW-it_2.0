#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

print 'Adesso    :', datetime.datetime.now()
print 'Oggi      :', datetime.datetime.today()
print 'UTC adesso:', datetime.datetime.utcnow()

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print attr, ':', getattr(d, attr)