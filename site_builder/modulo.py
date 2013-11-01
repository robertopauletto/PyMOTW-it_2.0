#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Costruisce le pagine indice
Versione %s %s
""" % ( __version__, __date__ )

import sys
sys.path.append(r'../lib')
from common import ottieni_moduli_tradotti

class Modulo(object):
    def __init__(self, nome):
        self.nome = nome
        self.versione = None
        self.titolo = ''
        self.descrizione = ''
        self.data_agg = None
        self.url = nome + '.html'


def elenco_per_indice():
    elenco = []
    for k, v in ottieni_moduli_tradotti().iteritems():
        modulo = Modulo(k)
        isinstance(modulo, Modulo)
        modulo.data_agg = v['agg']
        modulo.descrizione = v['descr']
        modulo.titolo = v['titolo']
        modulo.versione = v['versione']
        elenco.append(modulo)
    return elenco
        