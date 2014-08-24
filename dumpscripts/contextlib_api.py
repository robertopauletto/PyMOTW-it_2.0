#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Context(object):

    def __init__(self):
        print '__init__()'

    def __enter__(self):
        print '__enter__()'
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__()'
        
with Context():
    print 'Lavoro eseguito nel contesto'
