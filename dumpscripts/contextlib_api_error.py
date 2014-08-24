#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Context(object):

    def __init__(self, handle_error):
        print '__init__(%s)' % handle_error
        self.handle_error = handle_error

    def __enter__(self):
        print '__enter__()'
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__(%s, %s, %s)' % (exc_type, exc_val, exc_tb)
        return self.handle_error
        
with Context(True):
    raise RuntimeError('messaggio di errore gestito')

print

with Context(False):
    raise RuntimeError('messaggio di errore gestito')