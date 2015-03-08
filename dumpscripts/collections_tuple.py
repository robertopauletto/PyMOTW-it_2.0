#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

bob = ('Bob', 30, 'maschio')
print 'Rappresentazione:', bob

jane = ('Jane', 29, 'femmina')
print '\nCampo riferito da indice:', jane[0]

print '\nCampi riferiti da indice:'
for p in [ bob, jane ]:
    print '%s ha %d anni, %s' % p