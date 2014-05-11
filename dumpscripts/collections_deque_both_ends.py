#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections
import threading
import time

candle = collections.deque(xrange(11))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print '%8s: %s' % (direction, next)
            time.sleep(0.1)
    print '%8s fatto' % direction
    return

left = threading.Thread(target=burn, args=('Sinistra', candle.popleft))
right = threading.Thread(target=burn, args=('Destra', candle.pop))

left.start()
right.start()

left.join()
right.join()