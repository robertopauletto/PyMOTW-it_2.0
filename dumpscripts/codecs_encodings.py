from codecs_to_hex import to_hex

text = u'pi: p'

print 'Raw   :', repr(text)
print 'UTF-8 :', to_hex(text.encode('utf-8'), 1)
print 'UTF-16:', to_hex(text.encode('utf-16'), 2)