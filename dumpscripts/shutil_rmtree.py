from shutil import *
from commands import *

print 'PRIMA:'
print getoutput('ls -rlast /tmp/esempio')
rmtree('/tmp/esempio')
print 'DOPO :'
print getoutput('ls -rlast /tmp/esempio')
