#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
print 'Deindentato:\n'
print dedented_text
