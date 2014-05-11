#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

t = datetime.time(1, 2, 3)
print t
print 'ora    :', t.hour
print 'minuto :', t.minute
print 'secondo:', t.second
print 'microsecondo:', t.microsecond
print 'info fuso orario:', t.tzinfo
