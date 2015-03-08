#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='02/11/2013'
__version__='2.0'

__doc__ = """

Note sui file di traduzione da elaborare
========================================

Quando ho iniziato avevo pochissima esperienza in python

Il file da elaborare è in formato pseudo xml, non è ben formato e
contiene tag che **NON** devono essere elaborati in quanto rappresentano
codice di esempio quindi non mi avvalgo di alcun modulo che elabori
file xml tipo lxml o BeautifulSoup.

I file sono stati così creati in
quanto il progetto è individuale e volevo un file sorgente abbastanza
leggibile e facile da elaborare. La condizione fondamentale, infatti,
è che ogni tag che rappresenta una porzione di testo da rendere in
HTML sia sempre da solo **ad inizio riga**

Versione %s %s
""" % ( __version__, __date__ )


import os.path
import codecs
import traceback
import re
from functools import partial
from shutil import copyfile
from django.utils.encoding import smart_text
import my_html

h = my_html.MyHtml()  # Si occupa del rendering in HTML dei dati

DEF_CHARSET='utf-8'

TESTSDIR = os.path.abspath(os.path.dirname(__file__))
TEST_XML_FILE = r'/home/robby/Dropbox/Code/python/pymotw-it/tran/abc.xml'
HTML_OUTPUT = 'xmt2html_test.html'


# Lista dei tag - serve ad is_my_tag() per accertarsi di avere trovato un 
# MIO tag e non un pezzo di codice od altro
MY_TAGS = {
    'avvertimento': partial(h.warning),
    'categoria': None, 
    'descrizione': None,
    'deflist': partial(h.dl),
    'incipit': None, 
    'inserito_il': None, 
    'lista': partial(h.ul),
    'lista_ordinata': partial(h.ol),
    'lista_ricorsiva': partial(h.ul),
    'mk_xml_code': partial(h.code_xml, class_='well pre-scrollable'),
    'mk_xml_code_lineno': partial(
        h.code_xml_with_lineno, class_='well pre-scrollable'
        ),
    'note': partial(h.note),
    'py_code': partial(h.code, class_='well pre-scrollable'),
    'py_code_lineno': partial(h.code_with_lineno, class_='well pre-scrollable'),
    'py_output': partial(h.output_console, class_='well pre-scrollable'),
    'sottotitolo': partial(h.h4),
    'sql_code': partial(h.code_sql, class_='well pre-scrollable'),
    'tabella_semplice': partial(h.table, with_header=True, class_='table'),
    'tabella_1': None,
    'testo_normale': partial(h.p), 
    'titolo_1': None,
    'titolo_2': partial(h.h2),
    'titolo_3': partial(h.h3),
    'titolo_4': partial(h.h4),
    'vedi_anche': partial(h.biblio, class_='well'),
}

MY_TAG_KEYS = MY_TAGS.keys()
def is_my_tag(tag):
    """(str) -> bool
    
    Cerca `tag`  nella lista dei tag ammessi, ritorna True se trovato
    
    Precondizione: `tag` deve essere *lowercase*
    """
    return re.sub(r'>|<|/', '', tag.strip()) in MY_TAG_KEYS

RE_TAG_START = re.compile('^\<\w+\>')
RE_TAG_END = re.compile('^\<\/\w+\>')

RE_STRIP_TAG = re.compile(r'[<>/]')    
def pulisci_tag(tag):
    """(str) -> str
    
    Pulisce `tag` per ottenere il nome del tag senza parentesi
    """
    assert isinstance(tag, basestring)
    return RE_STRIP_TAG.sub('', tag.strip())

entities = { "à":"&agrave;", "è":"&egrave;", "ì":"&igrave;", "ò":"&ograve;", "ù":"&ugrave;" }
def text2entity(file_name):
    log = []
    if not os.path.exists(file_name):
        raise IOError("Manca " + file_name)    
    copyfile(file_name, file_name + ".bak")
    buffer = open(file_name, "r").read()
    for k,v in entities.iteritems():
        log.append( "Sostituzione di %s con %s " % (k,v))
        buffer = buffer.replace(k,v)
    open(file_name, 'w').write(buffer)    
    return "\n".join(log)

def load(xml_file):
    """(str) -> list of dict 
    
    Legge il contenuto di `xml_file` filtrando le righe con commenti
    Ritorna una lista composta da un dizionario:
    
    - chiave -> contiene il nome del tag
    - buffer -> contiene le righe da trasporre in html con il tag chiave

    Prerequisito: Tutti i tag per l'estrazione degli elementi sono di
    apertura e chiusura e **devono** essere da soli su di una sola riga.
    
    Sono ammessi tag di commento a patto che si trovino su di una sola riga
    """
    seq_elementi = []  # Conterrà elementi di dizionario 'tag': righe
    buffer = []  # Le righe da assegnare ad un tag ancora aperto
    is_aperto = False  # Se true la riga viene aggiunta al buffer del tag
    tag = ''  # conserva il nome del tag da utilizzare come chiave nel diz
    righe = []
    for riga in [riga.rstrip() for riga in
                 codecs.open(xml_file, encoding='utf-8').readlines()
                 if riga and not riga.startswith('<!--')]:    
        if RE_TAG_START.match(riga) and is_my_tag(riga.lower()):
            is_aperto = True
            tag = pulisci_tag(riga.lower())
        elif RE_TAG_END.match(riga) and is_my_tag(riga.lower()):
            seq_elementi.append({'tag': tag, 'buffer': buffer})
            buffer = []
            tag = ''
            is_aperto = False
        else:
            if is_aperto:
                buffer.append(riga)
    # Visto che i tag sono sempre di apretura/chiusura non mi preoccupo
    # di svuotare il buffer
    return seq_elementi

def check_my_tags(seq_elementi):
    """(dict) -> list of string
    
    Verifica se la chiave 'tag' in `seq_elementi` è un tag riconosciuto per
    la conversione in html. Ritorna una lista degli elementi non trovati
    
    Utilizzare prima di costruire la pagina per verificare errori di
    sintassi dei tag del file xml
    """
    not_found = []
    for item in seq_elementi:
        tag = item['tag']
        if not is_my_tag(tag):
            not_found.append(tag)
    return not_found

# In produzione questo sparisce
TEMP_FATTI = ('titolo_2', 'titolo_3', 'titolo_4', 'testo_normale',
              'lista', 'py_code', '', 
              'py_output', 'vedi_anche', 'tabella_semplice', 'mk_xml_code', 
              'avvertimento', 'note', 'titolo_3', 'deflist', 'sql_code', 
              'sottotitolo', 'lista_ricorsiva', 'py_code_lineno',
              'mk_xml_code_lineno', 'lista_ordinata')
def prepara_articolo(seq_elementi, tag_da_indicizzare=('titolo_2', 'titolo_3')):
    """(list of str, tuple of str) -> list, list
    
    Prepara il codice html per la pagina del modulo
    
    Ritorna:
    
    - il codice per l'indice nella barra destra
    - il codice per il contenuto dell'articolo
    """
    indice = []
    contenuti = []
    prg = 0
    for item in seq_elementi:
        tag = item['tag']
        if  is_my_tag(tag):
            if  tag in tag_da_indicizzare:
                item['a_name'] = h.a_name(str(prg))
                b = " ".join(item['buffer'])
                if '3' in tag:
                    b = "&nbsp;&nbsp;&nbsp;&nbsp;" + b
                indice.append(
                    h.a(
                        "#"+str(prg), smart_text(b, encoding='utf-8')
                    )
                )
                #indice.append(h.a("#"+str(prg), smart_text(b, encoding='utf-8')))
                contenuti.append(h.section(str(prg)))
                prg += 1
            if tag in TEMP_FATTI:
                codice=MY_TAGS[tag](item['buffer'] )
                contenuti.append(codice)
            else:
                print tag, "da gestire"
        else:
            print tag
    return indice, contenuti    

            

def render_articolo(file_xml):
    """(str) -> list, list
    
    Prepara il file html con l'articolo per il modulo contenuta in
    `file_xml`
    """
    seq_elementi = load(file_xml)
    indice_articolo, contenuti = prepara_articolo(seq_elementi)
    return indice_articolo, contenuti


def test_partial():
    h2 = functools.partial(h.h2)
    print h2("testo h2")

if __name__ == '__main__':
    print __doc__
    test_partial()