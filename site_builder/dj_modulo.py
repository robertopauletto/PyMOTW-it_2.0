#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )

from modulo import Modulo

class DjModulo(object):
    def __init__(self, indice, corpo, modulo):
        self._indice_sidebar = indice
        self._corpo = corpo
        self.modulo = modulo
        isinstance(self.modulo, Modulo)
        
    @property
    def titolo(self):
        return " - ".join((self.modulo.nome, self.modulo.titolo))
    
    @property
    def descrizione(self):
        return self.modulo.descrizione
    
    @property
    def versione(self):
        return self.modulo.versione
    
    @property
    def indice_laterale(self):
        return self._indice_sidebar

    @property
    def main_content(self):
        return "\n".join(self._corpo)


if __name__ == '__main__':
    print __doc__