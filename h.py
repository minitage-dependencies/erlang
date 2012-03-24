#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

import os

def p(op, bu):
    import pdb;pdb.set_trace()  ## Breakpoint ##
    os.system('chmod +x %s' % op['compile-directory']+'/configure')

# vim:set et sts=4 ts=4 tw=80:
