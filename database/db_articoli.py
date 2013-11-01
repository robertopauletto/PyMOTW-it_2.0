#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )

from collections import namedtuple
import sqlite3

def nuovo_articolo(db, articolo):
    q = """INSERT INTO articoli
           (data_pubb, nomefile, descrizione, categoria)
           VALUES (:dp, :nf, :des, :cat)"""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.exceute(q, articolo)





if __name__ == '__main__':
    print __doc__