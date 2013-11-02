#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )


import os.path
import datetime
import traceback

from math import ceil
from django import template
from django.template import loader

from dj_indice import Indice
from modulo import Modulo, elenco_per_indice

TEMPLATE_DIRS = ['../templates']
TEMPLATE_INDEX_NAME = 'index.html'
HTML_DIR = r'../html'
INDICE_MODULI_PER_PAGINA = 12
FILE_INDICE = 'index'
HTML_EXT = '.html'

def imposta_param_django(template_dirs):
    """(list of str)
    
    Imposta i parametri di configurazione per django ed assegna i
    percorsi per i file template in `template_dirs`
    """
    from django.conf import settings
    if  not settings.configured:
        settings.configure(
            DEBUG=True, TEMPLATE_DEBUG=True, 
            TEMPLATE_DIRS=(template_dirs),
            INSTALLED_APPS=(
                'django.contrib.markup',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.messages',
                ),
        )

def build(template_file, context_dict, rendered_file):
    """(str, dict, str)
    
    Rendering in `rendered_file` dalla pagina template `template_file`
    utilizzando gli elementi in `context`
    """
    try:
        t = loader.get_template(template_file)
        open(rendered_file, mode='w').write(
            t.render(template.Context(context_dict))
        )
    except Exception as ex:
        print traceback.format_exc()


def chunks(l, n):
    """(list, int)
    
    Ritorna blocchi di `n` elementi in `l`
    """
    return [l[i:i+n] for i in range(0, len(l), n)]

def crea_pagine_indice(template_dirs, template_name, file_indice):
    """(list of str, str, str)
    
    Crea le pagine indice
    """
    imposta_param_django(template_dirs)
    gm = []
    prg = 0
    moduli =  elenco_per_indice()
    pagine = ceil(len(moduli) / INDICE_MODULI_PER_PAGINA)
    print pagine
    for gruppo_moduli in chunks(moduli, INDICE_MODULI_PER_PAGINA):
        for m in gruppo_moduli:
            gm.append(m)
        i = Indice(gm)
        if ((prg + 1) < pagine):
            i.prev_nr_page = prg + 1
        dic = {'indice': i,}
        fn = '%s%s.html' % (file_indice, "_" + str(prg) if prg else '')
        build(template_name, dic, os.path.join(HTML_DIR, fn))
        prg += 1
        gm = []



if __name__ == '__main__':
    print __doc__
    crea_pagine_indice(TEMPLATE_DIRS, TEMPLATE_INDEX_NAME, FILE_INDICE)
    print "Ok"