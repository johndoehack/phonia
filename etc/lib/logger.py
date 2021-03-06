#!/usr/bin/env python3

import sys
import os
from lib.args import args

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        out = args.output
        import os
        import os.path

        if args.output[0] != '/':
            output = os.environ['OLDPWD']+'/'+args.output
        else:
            output = args.output
            
        self.log = open(output, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass
