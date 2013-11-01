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
HTML_DIR = r'../html'

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

def main(template_dirs):
    imposta_param_django(template_dirs)
    #m = Modulo('codecs')
    #m.data_agg = datetime.date(2013, 10, 1)
    #m.descrizione = 'Descrizione del modulo codecs'
    #m.titolo  = 'il modulo codecs'
    #m.versione = '2.1'
    gm = []
    #for i in range(12):
        #gm.append(m)
    prg = 0
    fn_index = 'index'
    fn_ext = '.html'
    moduli =  elenco_per_indice()
    pagine = ceil(len(moduli) / 12)
    print pagine
    for gruppo_moduli in chunks(moduli, 12):
        for m in gruppo_moduli:
            gm.append(m)
            i = Indice(gm)
            if ((prg + 1) < pagine):
                i.prev_nr_page = prg + 1
            dic = {'indice': i,}
            fn = '%s%s.html' % (fn_index, "_" + str(prg) if prg else '')
            build('index.html', dic, os.path.join(HTML_DIR, fn))
        prg += 1
        gm = []



if __name__ == '__main__':
    print __doc__
    main(TEMPLATE_DIRS)
    print "Ok"