#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile
import os

os.mkdir('outdir')
t = tarfile.open('esempio.tar', 'r')
t.extractall('outdir', members=[t.getmember('LEGGIMI.txt')])
print os.listdir('outdir')
