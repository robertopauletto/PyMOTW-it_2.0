#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib

from imaplib_connect import open_connection

if __name__ == '__main__':
    c = open_connection()
    try:
        typ, data = c.list(pattern='*Archive*')
    finally:
        c.logout()
    print 'Codice risposta:', typ

    for line in data:
        print 'Risposta del server:', line