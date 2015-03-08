#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Queue

q = Queue.Queue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print q.get()
    