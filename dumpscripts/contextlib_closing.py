#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import contextlib

class Door(object):
    def __init__(self):
        print '  __init__()'
    def close(self):
        print '  close()'

print 'Esempio Normale:'
with contextlib.closing(Door()) as door:
    print '  dentro l\'istruzione with'

print
print 'Esempio di gestione errore:'
try:
    with contextlib.closing(Door()) as door:
        print '  sollevata da dentro l\'istruzione with'
        raise RuntimeError('messaggio di errore')
except Exception, err:
    print '  Si è verificato un errore:', err