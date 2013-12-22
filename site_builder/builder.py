#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

__date__=''
__version__='0.1'
__doc__="""
Il punto di entrata dell'applicazione (nella modalità console)

Da qui vengono costruite le singole pagine, gli indici e le tabelle
riepilogative

Le pagine vengono costruite basandosi su bootstrap 3

Versione %s %s
""" % ( __version__, __date__ )

try:
    import codecs
    import os.path
    import os
    import sys
    import datetime
    import traceback
    
    from math import ceil
    from django import template
    from django.template import loader
    
    from dj_indice import Indice
    from dj_modulo import DjModulo
    from dj_tabelle_indici import DjTabelleIndici
    from modulo import Modulo, elenco_per_indice
    import modulo_xml2html 
    from index_builder import ottieni_tabella
    sys.path.append(r'../lib')
    from common import clear_console
    from footer import Footer
except ImportError as imperr:
    raise Exception("Errore importazione modulo\n\n" + imperr.message)

DEF_CHARSET='utf-8'

TEMPLATE_DIRS = ['../templates']
TRAN_DIR = r'../tran'
TEMPLATE_INDEX_NAME = 'index.html'
TEMPLATE_MODULE_NAME = 'modulo.html'
TEMPLATE_TABALFA_NAME = 'tabella_moduli.html'
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
            codecs.encode(t.render(
                template.Context(context_dict)), DEF_CHARSET)
        )
    except Exception as ex:
        print traceback.format_exc()


def chunks(l, n):
    """(list, int)
    
    Ritorna blocchi di `n` elementi in `l`
    """
    return [l[i:i+n] for i in range(0, len(l), n)]

def crea_pagine_indice(template_name, file_indice):
    """(str, str)
    
    Crea le pagine indice, che contengono i teaser per 12 moduli ognuna
    """
    gm = []
    prg = 0
    moduli =  elenco_per_indice()
    pagine = ceil(len(moduli) / INDICE_MODULI_PER_PAGINA)
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

def crea_pagina_modulo(template_name, file_modulo, footer):
    """(str, str)
    
    Crea la pagina per un modulo.
    
    `template_name` è il nome del modello per il rendering
    `file_modulo` è il file xml dal quale ricavare la pagina html
    """
    #print modulo_xml2html.text2entity(file_modulo)
    
    indice, main_content = modulo_xml2html.render_articolo(file_modulo)
    fn = os.path.splitext(os.path.basename(file_modulo))[0]
    modulo = Modulo.ottieni_modulo(fn)
    m = DjModulo(indice, main_content, modulo, footer)
    fn += '.html'
    dic = {'modulo': m,}
    build(template_name, dic, os.path.join(HTML_DIR, fn))

def crea_tabella_indice(template_name):
    """(str)
    
    Crea la pagina che contiene la tabella che riepiloga tutti i moduli

    `template_name` è il nome del modello per il rendering
    """
    moduli = elenco_per_indice()
    #corpo = ottieni_tabella(moduli)
    m = DjTabelleIndici(moduli)
    fn = 'indice_alfabetico.html'
    dic = {'modulo': m,}
    build(template_name, dic, os.path.join(HTML_DIR, fn))
    


        
FOOTER = Footer(
    'PyMOTW-it',
    periodo='2013',
    data_agg=datetime.date.today().strftime("%d-%m-%Y")
)    

if __name__ == '__main__':
    print __doc__
    parms = sys.argv
    if not len(parms) == 2:
        exit(0)
    clear_console
    # Per prima cosa si impostano i parametri per django
    imposta_param_django(TEMPLATE_DIRS)
    dummy, choice = parms
    if choice.lower().startswith('ind'):
        crea_pagine_indice(TEMPLATE_INDEX_NAME, FILE_INDICE)
    elif choice.lower().startswith('tab'):
        crea_tabella_indice(TEMPLATE_TABALFA_NAME)
    else:
        if not os.path.splitext(choice)[1]:
            choice += '.xml'
            choice = os.path.join(TRAN_DIR, choice)
            if not os.path.exists(choice):
                exit(0)
            print "Costruzione pagina in corso ..."
            crea_pagina_modulo(TEMPLATE_MODULE_NAME, choice, FOOTER)
    
    
    print "Fine"