#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc
from abc_base import PluginBase

class RegisteredImplementation(object):
    
    def load(self, input):
        return input.read()
    
    def save(self, output, data):
        return output.write(data)

PluginBase.register(RegisteredImplementation)

if __name__ == '__main__':
    print 'Sottoclasse:', issubclass(RegisteredImplementation, PluginBase)
    print 'Istanza    :', isinstance(RegisteredImplementation(), PluginBase)