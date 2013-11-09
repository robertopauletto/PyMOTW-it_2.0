#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )

import codecs
import os.path
import datetime
import traceback

from math import ceil
from django import template
from django.template import loader

from dj_indice import Indice
from dj_modulo import DjModulo
from modulo import Modulo, elenco_per_indice
import modulo_xml2html 

DEF_CHARSET='utf-8'

TEMPLATE_DIRS = ['../templates']
TEMPLATE_INDEX_NAME = 'index.html'
TEMPLATE_MODULE_NAME = 'modulo.html'
HTML_DIR = r'../html'
INDICE_MODULI_PER_PAGINA = 12
FILE_INDICE = 'index'
HTML_EXT = '.html'
TEST_XML_FILE = r'/home/robby/Dropbox/Code/python/pymotw-it/tran/abc.xml'

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
            codecs.encode(t.render(template.Context(context_dict)), 'utf-8')
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

def crea_pagina_modulo(template_dirs, template_name, file_modulo):
    indice, main_content = modulo_xml2html.render_articolo(file_modulo)
    fn = os.path.splitext(os.path.basename(file_modulo))[0]
    modulo = Modulo.ottieni_modulo(fn)
    m = DjModulo(indice, main_content, modulo)
    fn = 'test_modulo.html'
    dic = {'modulo': m,}
    build(template_name, dic, os.path.join(HTML_DIR, fn))

if __name__ == '__main__':
    print __doc__
    # Creazione di tutte le pagine indice
    #crea_pagine_indice(TEMPLATE_DIRS, TEMPLATE_INDEX_NAME, FILE_INDICE)
    
    # Creazione di un modulo
    imposta_param_django(TEMPLATE_DIRS)
    crea_pagina_modulo(TEMPLATE_DIRS, TEMPLATE_MODULE_NAME, TEST_XML_FILE)
    
    print "Ok"