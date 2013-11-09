#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Metodi per la costruzione di codice html per le pagine di
moduli ed indice
Versione %s %s
""" % ( __version__, __date__ )

from inline_sub import InlineSubs
from collections import namedtuple
from ast import literal_eval
from pyg import colora_codice

class MyHtml(object):
    """Si occupa della costruzione di elementi HTML"""
    insubs = InlineSubs()
    AUTOCLOSING_TAGS = (
        'br',
        'hr',
    )
    
    def _get_tag(self, tag_name, **kwargs):
        """(str [, **kvargs]) -> str
        
        Genera `tag_name` che non richiede elemento di chiusura, tipo hr/br
        Gli eventuali parametri sono gli attributi letterali del tag
        (Nessun controllo viene effettuato)
        
        _get_tag('br' class='classe') ritorna:
        <br class=classe />
        """
        return "<%s %s />" % (tag_name, self._get_attrs(dict(kwargs)))
    
    def _get_attrs(self, dic):
        """(dict) -> str
        
        Ritorna gli elementi in dict nella sintassi chiave='valore'
        
        Si utilizza per gestire gli attributi di un tag
        """
        if not dic:
            return ''
        attrs = ['']
        for k, v in dic.iteritems():
            if 'class' in k:
                k = 'class'
            attrs.append("%s='%s'" % (k, v))
        return ' '.join(attrs)    
    
    def _get_start_end_tag(self, tag_name, value='', **kwargs):
        """(str, str [**wkargs]) -> str

        Genera il tag HTML `tag_name` ed il suo contenuto
        Gli eventuali parametri sono gli attributi letterali del tag
        (Nessun controllo viene effettuato)
        """
        return "<%s%s>%s</%s>" % (
            tag_name,
            self._get_attrs(dict(kwargs)),
            value,
            tag_name
        )

    def _convert(self, value, char_sep = ' '):
        """(object) -> str
        
        Se `value` è una stringa unisce gli elementi separandoli con uno
        spazio.
        
        Si utilizza in quanto il valore da rendere in html viene in genere
        passato attraverso una lista, ad esempio per generare elementi li
        oppure tabelle
        """
        if isinstance(value, basestring):
            pass
        elif isinstance(value, list) or isinstance(value,  tuple):
            value = char_sep.join(value)
        else:
            value = str(value)
        return MyHtml.insubs.rimpiazza(value)

    def _lista(self, value, is_ordered=False, **kwargs):
        assert isinstance(value, list) or isinstance(value, tuple)
        acc = []
        tag = "ul" if not is_ordered else "ol"
        for row in value:
            acc.append(self._get_start_end_tag(
                "li",
                self._convert(row),
                **kwargs
            ))
        return self._get_start_end_tag(tag, " ".join(acc))
    
    def _codice(self, value, **kwargs):
        return colora_codice(value)
        
    def _vedi_anche(self, lista, dd_class=None, **kwargs):
        """(list [,str]) ->
        
        Rappresentazione di riferimenti bibliografici e interconnessioni
        
        Si estrinseca in una definition list con definizione il link
        della risorsa e descrizione la descrizione della risorsa medesima
        
        `dd_class` è un eventuale codice css da applicare al tag *dd*
        
        Precondizione: `value` deve essere una lista i cui valori, separati
        dal carattere **pipe** rappresentano rispettivamente:
        
        - url
        - descrizione url
        - descrizione risorsa
        
        l'ultimo valore può anche mancare, in tal caso viene recuperato
        dalla descrizione dell'url
        """
        assert isinstance(lista, list)
        Biblio = namedtuple('Biblio', 'url,desc,definiz')
        output = [""]
        ddargs = {}
        if dd_class:
            ddargs['class'] = dd_class
        for riga in [riga.split("|") for riga in lista]:
            biblio = Biblio(*riga)
            u = self.a(biblio.url, biblio.desc)
            output.append(self._get_start_end_tag('dt', u))
            output.append(self._get_start_end_tag('dd', biblio.definiz, **ddargs))
        output.append("")
        return self._get_start_end_tag('dl',"\n".join(output))
            
    # --------------------------------------------------------------------
    # METODI DI CONVENIENZA PER IL RENDERING DI SPECIFICI TAGS
    # I consumatori della classe dovrebbero utilizzare solo questi metodi
    # --------------------------------------------------------------------
    
    def h1(self, value, **kwargs):
        return self._get_start_end_tag('h1', value, **kwargs)

    def h2(self, value, **kwargs):
        return self._get_start_end_tag('h2', self._convert(value), **kwargs)
    
    def h3(self, value, **kwargs):
        return self._get_start_end_tag('h3', value, **kwargs)

    def h4(self, value, **kwargs):
        return self._get_start_end_tag('h4', value, **kwargs)

    def h5(self, value, **kwargs):
        return self._get_start_end_tag('h5', value, **kwargs)

    def p(self, value, **kwargs):
        return self._get_start_end_tag('p', self._convert(value), **kwargs)

    def strong(self, value, **kwargs):
        return self._get_start_end_tag('strong', self._convert(value), **kwargs)

    def a(self, url, value, **kwargs):
        kwargs['href'] = "%s" % url
        return self._get_start_end_tag('a', value, **kwargs)

    def a_name(self, id, value='', **kwargs):
        kwargs['name'] = id
        return self._get_start_end_tag('a', value, **kwargs)
    
    def ul(self, value, **kwargs):
        return self._lista(value, is_ordered=False, **kwargs)
    
    def code(self, value, **kwargs):
        pigmentato = self._codice(value)
        return self._get_start_end_tag('div', pigmentato, **kwargs)
    
    def output_console(self, value, **kwargs):
        """(str) -> str
        
        Mostra l'output console"""
        testo = self._convert(value, "\n")
        return self._get_start_end_tag('pre', testo, **kwargs)
    
    def biblio(self, value, dd_class='indent', **kwargs):
        header = self.p(self.strong('Vedere anche:'))
        dl = self._vedi_anche(value, dd_class)
        return self._get_start_end_tag('div', header + dl, **kwargs)    
    
if __name__ == '__main__':
    print __doc__
    h = MyHtml()
    print h.h3('tag h3', id=123)
    print h.h1('tag h1')
    #print h.a('www.python.org', 'Python!', title='sito python')
    #print h.a_name('tag a name')
    lista = [
        'http://docs.python.org/library/abc.html|abc|La documentazione della libreria standard per questo modulo', 
        'http://www.python.org/dev/peps/pep-3119|PEP 3119|Introduzione alle classi base astratte', 
        'http://docs.python.org/library/collections.html|collections|La documentazione della libreria standard per le collezioni'
    ]
    print h._vedi_anche(lista)