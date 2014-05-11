#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc
from abc_base import PluginBase

class IncompleteImplementation(PluginBase):
    
    def save(self, output, data):
        return output.write(data)

PluginBase.register(IncompleteImplementation)

if __name__ == '__main__':
    print 'Sottoclasse:', issubclass(IncompleteImplementation, PluginBase)
    print 'Istanza    :', isinstance(IncompleteImplementation(), PluginBase)    