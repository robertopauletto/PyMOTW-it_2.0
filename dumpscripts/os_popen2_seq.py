#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

print 'popen2, comandi in sequenza:'
pipe_stdin, pipe_stdout = os.popen2(['cat', '-'])
try:
    pipe_stdin.write('attraverso stdin allo stdout')
finally:
    pipe_stdin.close()
try:
    stdout_value = pipe_stdout.read()
finally:
    pipe_stdout.close()
print '\tpassa attraverso:', repr(stdout_value)


