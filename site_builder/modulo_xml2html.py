#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='02/11/2013'
__version__='0.1'

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
HTML sta sempre da solo **ad inizio riga**

Versione %s %s
""" % ( __version__, __date__ )


import unittest
import os.path
import codecs
import traceback
import re

TESTSDIR = os.path.abspath(os.path.dirname(__file__))
TEST_XML_FILE = r'/home/robby/Dropbox/Code/python/pymotw-it/tran/abc.xml'
HTML_OUTPUT = 'xmt2html_test.html'

# Lista dei tag - serve ad is_my_tag() per accertarsi di avere trovato un 
# MIO tag e non un pezzo di codice od altro
MY_TAGS = [
    'avvertimento',
    'categoria', 
    'descrizione',
    'deflist',
    'incipit', 
    'inserito_il', 
    'lista', 
    'lista_ricorsiva',
    'mk_xml_code',
    'mk_xml_code_lineno',
    'note',
    'py_code',
    'py_code_lineno',
    'py_output',
    'sottotitolo',
    'sql_code', 
    'tabella_semplice',
    'tabella_1',
    'testo_normale', 
    'titolo_1',
    'titolo_2',
    'titolo_3',
    'vedi_anche',
    
]
def is_my_tag(tag):
    """(str) -> bool
    
    Cerca `tag`  nella lista dei tag ammessi, ritorna True se trovato
    """
    return re.sub(r'>|<|/', '', tag.strip()) in MY_TAGS

RE_TAG_START = re.compile('^\<\w+\>')
RE_TAG_END = re.compile('^\<\/\w+\>')

RE_STRIP_TAG = re.compile(r'[<>/]')    
def pulisci_tag(tag):
    """(str) -> str
    
    Pulisce `tag` per ottenere il nome del tag senza parentesi
    """
    assert isinstance(tag, basestring)
    return RE_STRIP_TAG.sub('', tag.strip())


def load(xml_file):
    """(str) -> list of dict 
    
    Legge il contenuto di `xml_file` filtrando le righe con commenti
    Ritorna una lista composta da un dizionario con chiave il nome del tag
    e valore le righe da trasporre il html con il tag chiave
    

    Prerequisito: Tutti i tag per l'estrazione degli elementi sono di
    apertura e chiusura e **devono** essere da soli su di una sola riga.
    
    Sono ammessi tag di commento a patto che si trovino su di una sola riga
    """
    seq_elementi = []  # Conterrà elementi di dizionario 'tag': righe
    buffer = []  # Le righe da assegnare ad un tag ancora aperto
    is_aperto = False  # Se true la riga viene aggiunta al buffer del tag
    tag = ''  # conserva il nome del tag da utilizzare come chiave nel diz
    for riga in [riga.strip() for riga in
                 codecs.open(xml_file, encoding='utf-8').readlines()
                 if riga and not riga.startswith('<!--')]:
        if RE_TAG_START.match(riga) and is_my_tag(riga):
            is_aperto = True
            tag = pulisci_tag(riga)
        elif RE_TAG_END.match(riga) and is_my_tag(riga):
            seq_elementi.append({tag: buffer})
            buffer = []
            tag = ''
            is_aperto = False
        else:
            if is_aperto:
                buffer.append(riga)
    return seq_elementi

class ClassTest(unittest.TestCase):
    """ Classe per test """
    def setUp(self):
        self.xml = TEST_XML_FILE
    
    def tearDown(self):
        pass
    
    def test_load(self):
        seq = load(TEST_XML_FILE)
        self.assertTrue(len(seq) > 0)
    


if __name__ == '__main__':
    print __doc__
    import sys
    suite = unittest.TestSuite()
    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(ClassTest)
    else:
        for nome_test in sys.argv[1:]:
            suite.addTest(ClassTest(nome_test))
        
    unittest.TextTestRunner(verbosity=2).run(suite)