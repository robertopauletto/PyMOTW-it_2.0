#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priorita, dettagli, stato, scadenza from compito where progetto = 'pymotw-it'
    """)

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print '%2d {%d} %-20s [%-8s] (%s)' % (task_id, priority, details, status, deadline)