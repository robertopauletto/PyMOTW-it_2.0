#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Utility varie 
Versione %s %s
""" % ( __version__, __date__ )

from os import name
import sys 
import os.path 
import datetime

sys.path.append(r'../database')

PATHS = {
    'posix': r'/home/robby',
    'mac':  r'/Users/robby',
    'win32': r'c:\users\robby',
}

OLD_HTML_FOLDER = r'Dropbox/Code/python/pymotw-it/html'
OLD_TRAN_FOLDER = r'Dropbox/Code/python/pymotw-it/tran'

def get_root(paths=PATHS, fixed_path=''):
    """
    Ritorna la radice del percorso di lavoro in base al sistema
    operativo in cui viene eseguito lo script, scegliendo tra i
    valori in `paths`
    
    >>> get_root()
    '/home/robby/'
    >>> print get_root(fixed_path='subfolder/subfolder1')
    /home/robby/subfolder/subfolder1
    """
    if sys.platform == 'darwin':
        return os.path.join(paths['mac'], fixed_path )
    if name in paths.keys():
        return os.path.join(paths[name], fixed_path )
    else:
        return os.path.join('.', fixed_path)


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

def get_xml_files():
    """
    Metodo di convenienza che estrae i percorsi completi dei file xml
    con la traduzione
    
    Modificare la variabile `OLD_TRAN_FOLDER` per impostare la directory
    dove sono contenuti i file
    """
    return [
        os.path.splitext(os.path.basename(f))[0]
        for f in os.listdir(xml_path())
        if f.endswith('.xml')
    ]

def get_html_files():
    """
    Metodo di convenienza che ritorna i percorsi completi dei file
    html con la traduzione

    Modificare la variabile `OLD_HTML_FOLDER` per impostare la directory
    dove sono contenuti i file
    """
    html_files = [
        os.path.splitext(os.path.basename(f))[0]
        for f in os.listdir(html_path())
        if f.endswith('.html') and not 'index' in f
    ]
    
def _estrai_da_tag(righe, nome_tag, ripeti=False):
    """(list of str, str [,bool]) -> list of str
    
    Scansione `righe` e ritorna il testo racchiuso tra `tag` 1 sola volta
    se `ripeti` == `True`
    
    Da utilizzare per recuperare valori di tag univoci tipo descrizione
    """
    nome_tag = "%s" % nome_tag
    retval = []
    is_aperto = False
    for riga in righe:
        if riga[1:].startswith(nome_tag):
            if not is_aperto:
                is_aperto = True
        elif riga[2:].startswith(nome_tag):
            is_aperto = False
            if not ripeti:
                return retval
        else:
            if is_aperto:
                retval.append(riga.strip())
    return retval            
        
def ottieni_moduli_tradotti():
    """
    Ritorna un dizionario con chiave nome modulo che contiene:
    
    - data ultima modifica
    - titolo
    - versione
    - descrizione
    """
    retval = {}
    da_elaborare = get_xml_files()
    xml_dir = xml_path()
    for modulo in da_elaborare:
        fn = os.path.join(xml_dir, modulo+'.xml')
        if not os.path.exists(fn):
            print "Articolo non presente: %s" % os.path.basename(fn)
            continue
        righe = open(fn).readlines()
        descr, vers = _estrai_da_tag(righe, 'descrizione')
        titolo = " ".join(_estrai_da_tag(righe, 'titolo_1'))
        ultimo_agg = datetime.date.fromtimestamp(os.stat(fn).st_mtime)
        retval[modulo] = {  
            'descr': descr,
            'titolo': titolo.split('-')[1].strip(),
            'agg': ultimo_agg,
            'versione': vers,
        }
    return retval


if __name__ == '__main__':
    print __doc__
    print ottieni_moduli_tradotti()