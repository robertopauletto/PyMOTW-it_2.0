#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import array
import binascii
import tempfile

a = array.array('i', xrange(5))
print 'A1:', a

# Scrivo un array di cifre in un file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file) # devo passare un *vero* file
output.flush()

# Leggo i dati grezzi
input = open(output.name, 'rb')
raw_data = input.read()
print 'Contenuto grezzo:', binascii.hexlify(raw_data)

# Leggo i dati in un array
input.seek(0)
a2 = array.array('i')
a2.fromfile(input, len(a))
print 'A2:', a2
