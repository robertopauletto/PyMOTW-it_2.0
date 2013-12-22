#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Costruisce le pagine indice
Versione %s %s
""" % ( __version__, __date__ )

import sys
sys.path.append(r'../lib')
from common import ottieni_moduli_tradotti, ottieni_modulo
from inline_sub import InlineSubs

class Modulo(object):
    insubs = InlineSubs()
    def __init__(self, nome):
        self.nome = nome
        self.versione = None
        self.titolo = ''
        self.descrizione = ''
        self.data_agg = None
        self.url = nome + '.html'

    @staticmethod
    def ottieni_modulo(nome_modulo):
        diz = ottieni_modulo(nome_modulo)
        m = Modulo(nome_modulo)
        m.data_agg = diz['agg']
        m.descrizione = Modulo.insubs.rimpiazza(diz['descr'])
        m.titolo = diz['titolo']
        m.versione = diz['versione']
        return m
    
    def per_tabella_indice(self):
        return [
            self.data_agg.strftime('%d.%m.%Y'),
            self.nome,
            self.titolo
        ]

    

def elenco_per_indice():
    """Ritorna una lista di oggetti `:py:class:Modulo`
    """
    elenco = []
    insubs = InlineSubs()
    for k, v in ottieni_moduli_tradotti().iteritems():
        modulo = Modulo(k)
        isinstance(modulo, Modulo)
        modulo.data_agg = v['agg']
        modulo.descrizione = insubs.rimpiazza(v['descr'])
        modulo.titolo = v['titolo']
        modulo.versione = v['versione']
        elenco.append(modulo)
    return elenco
        