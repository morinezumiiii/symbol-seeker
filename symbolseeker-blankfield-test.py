#!/usr/bin/python
# -*- coding: utf-8
from symbolseeker import SymbolSeeker

target = 'test-image/test1.gif'

seeker = SymbolSeeker()
if seeker.blankfield(target, (610,141)):
    print 'failed: this is blank field'
else:
    print 'success: this is no blank field'

if seeker.blankfield(target, (610,180)):
    print 'success: this is blank field'
else:
    print 'failed: this is no blank field'

