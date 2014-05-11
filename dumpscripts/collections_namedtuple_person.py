#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

Person = collections.namedtuple('Person', 'name age gender')

print 'Tipo di Persona:', type(Person)

bob = Person(name='Bob', age=30, gender='maschio')
print '\nRappresentazione:', bob

jane = Person(name='Jane', age=29, gender='femmina')
print '\nCampo per nome:', jane.name

print '\nCampi per indice:'
for p in [ bob, jane ]:
    print '%s ha %d anni, %s' % p