#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import contextlib

@contextlib.contextmanager
def make_context():
    print '  in entrata'
    try:
        yield {}
    except RuntimeError, err:
        print '  ERRORE:', err
    finally:
        print '  in uscita'

print 'Normale:'
with make_context() as value:
    print '  dentro l\'istruzione with:', value

print
print 'Errore gestito:'
with make_context() as value:
    raise RuntimeError('si mostra un esempio di gestione di un errore')

print
print 'Errore non gestito:'
with make_context() as value:
    raise ValueError('questa eccezione non viene gestite')