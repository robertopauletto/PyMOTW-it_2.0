#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def load(self, input):
        """Recupera dati dalla sorgente in input e ritorna un oggetto"""
        return
    
    @abc.abstractmethod
    def save(self, output, data):
        """Salva l'oggetto dati in output."""
        return