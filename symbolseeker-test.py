#!/usr/bin/python
# -*- coding: utf-8 -*-
from symbolseeker import SymbolSeeker

seeker = SymbolSeeker()
symbol = 'test-image/symbol.gif'
target = 'test-image/test1.gif'
resume_xy = (0,0)

if seeker.seek(symbol, target, resume_xy):
    print str(seeker.position)
    print 'It is matched!'
else:
    print 'No match found.'
