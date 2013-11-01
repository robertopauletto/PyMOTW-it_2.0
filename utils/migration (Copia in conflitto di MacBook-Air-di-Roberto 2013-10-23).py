#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )

import codecs
import sys
import os.path
import re
from collections import defaultdict
sys.path.append(r'../lib')

from common import get_root

OLD_HTML_FOLDER = r'Dropbox/Code/python/pymotw-it/html'
OLD_TRAN_FOLDER = r'Dropbox/Code/python/pymotw-it/tran'

def html_path():
    """
    Metodo di convenienza che ottiene il percorso dei file html tradotti

    >>> print html_path()
    /home/robby/Dropbox/Code/python/pymotw-it/html
    """
    return get_root(fixed_path=OLD_HTML_FOLDER)

def xml_path():
    """
    Metodo di convenienza che ottiene il percorso dei file xml tradotti
    
    >>> print xml_path()
    /home/robby/Dropbox/Code/python/pymotw-it/tran
    """
    return get_root(fixed_path=OLD_TRAN_FOLDER)


def match_xml_html(output=False, sistema=False):
    """(bool, bool) -> list, list
    
    Confronto tra file xml ed html (evidenzia quelli non pubblicati)
    Rinomina i file xml ancora da pubblicare se `sistema` == `True`
    Ritorna i nomi dei file (senza suffisso) presenti nelle cartelle
    **tran** ed **html**
    """
    xml_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(xml_path())
                 if f.endswith('.xml')]
    html_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(html_path())
                 if f.endswith('.html') and not 'index' in f]
    if output:
        print "File xml  -> %d\nFile html -> %d" % (len(xml_files),  len(html_files))
    da_pubblicare = set.symmetric_difference(set(xml_files), set(html_files))
    if sistema:
        p = xml_path()
        for f in da_pubblicare:
            os.rename(os.path.join(p, f+'.xml'), os.path.join(p, f + ".da_tradurre"))
    return xml_files, html_files

def estrai_categoria():
    """
    Estrae la descrizione della categoria dai file html e ritorna
    un dizionare con chiave nome file (senza estensione) e valore la
    categoria rilevata
    """
    p = html_path()
    html_files = [os.path.join(p, f) for f in os.listdir(html_path())
             if f.endswith('.html') and not 'index' in f]
    retval = defaultdict(str)
    for f in html_files:
        categ = [riga.strip() for riga in open(f).readlines()
             if riga.startswith("<!-- Categoria")][0]
        categ = re.sub(r'[\<\>\-\!]', '', categ)
        retval[os.path.splitext(os.path.basename(f))[0]] = categ.split(':')[1]
    return retval
    
def scrivi_categoria_in_xml(elenco, diz_cat):
    xml_files = [os.path.join(xml_path(), f) 
                 for f in os.listdir(xml_path()) if f.endswith('.xml')]
    xml_dir = xml_path()
    for modulo in elenco:
        fn = os.path.join(xml_dir, modulo+'.xml')
        righe = open(fn).readlines()
        righe.insert(1, _componi_categoria(diz_cat[modulo]))
        #open(fn, mode='w' ).writelines(righe)
        print 
        
def _componi_categoria(descr):
    return "<categoria>\n%s\n</categoria>\n" % descr
    
if __name__ == '__main__':
    print __doc__
    #match_xml_html(True) 
    #estrai_categoria()
    scrivi_categoria_in_xml(match_xml_html()[0], estrai_categoria())