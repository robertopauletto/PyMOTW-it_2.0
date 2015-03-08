#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Queue

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'Nuovo Lavoro:', description
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()

q.put( Job(3, 'Lavoro Normale') )
q.put( Job(10, 'Lavoro non significativo') )
q.put( Job(1, 'Lavoro importante') )

while not q.empty():
    next_job = q.get()
    print 'Elaborazione dei lavori:', next_job.description
    