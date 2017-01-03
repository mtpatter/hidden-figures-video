#!/usr/bin/env python

"""Takes a textfile and slow types contents into
the terminal visualization created by terminal.py
(via commands.txt).

Usage:
python slowtyper.py textfile
"""

import sys
import time


def main(textfile, outfile):
    with open(textfile, 'r') as f:
        lines = f.read()

    alltext = ''
    for s in lines:
        alltext = alltext + s
        with open(outfile, 'w') as f:
            f.write(alltext)
        time.sleep(0.1)

if __name__ == '__main__':

    outfile = 'commands.txt'

    main(sys.argv[1], outfile)
