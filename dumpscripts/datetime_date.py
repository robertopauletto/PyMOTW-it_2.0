#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

today = datetime.date.today()
print today
print 'ctime:', today.ctime()
print 'tupla:', today.timetuple()
print 'ordinale:', today.toordinal()
print 'Anno:', today.year
print 'Mese:', today.month
print 'Giorno:', today.day
