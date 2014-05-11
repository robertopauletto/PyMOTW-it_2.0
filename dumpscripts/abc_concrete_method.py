#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc
from cStringIO import StringIO

class ABCWithConcreteImplementation(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def retrieve_values(self, input):
        print 'classe base che legge dati'
        return input.read()

class ConcreteOverride(ABCWithConcreteImplementation):
    
    def retrieve_values(self, input):
        base_data = super(ConcreteOverride, self).retrieve_values(input)
        print 'sottoclasse che ordina dati'
        response = sorted(base_data.splitlines())
        return response

input = StringIO("""riga uno
riga due
riga tre
""")

reader = ConcreteOverride()
print reader.retrieve_values(input)
print

#if __name__ == '__main__':
    #print 'Sottoclasse:', issubclass(IncompleteImplementation, PluginBase)
    #print 'Istanza    :', isinstance(IncompleteImplementation(), PluginBase)    