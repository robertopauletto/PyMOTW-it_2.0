#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pprint import pprint

class node(object):
    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents[:]
    def __repr__(self):
        return 'nodo(' + repr(self.name) + ', ' + repr(self.contents) + ')'

trees = [ node('nodo-1'),
         node('nodo-2', [ node('nodo-2-1')]),
         node('nodo-3', [ node('nodo-3-1')]),
         ]
pprint(trees)
