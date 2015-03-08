#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

try:
    collections.namedtuple('Persona', 'nome class anni genere')
except ValueError, err:
    print err

try:
    collections.namedtuple('Person', 'nome anni genere anni')
except ValueError, err:
    print err
    