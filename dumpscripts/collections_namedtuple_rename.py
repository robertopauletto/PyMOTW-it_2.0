#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

with_class = collections.namedtuple('Persona', 'nome class anni genere', rename=True)
print with_class._fields

two_ages = collections.namedtuple('Persona', 'nome anni genere anni', rename=True)
print two_ages._fields