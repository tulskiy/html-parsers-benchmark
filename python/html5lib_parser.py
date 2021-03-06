# -*- coding: utf-8 -*-
'''
Created on 2012-12-03

@author: Sergey Prokhorov <me@seriyps.ru>
'''
import html5lib

import time
import sys


def main():
    with open(sys.argv[1], 'r') as f:
        do_parse_test(f.read(), int(sys.argv[2]))


def do_parse_test(html, n):
    start = time.time()
    for i in xrange(n):
        tree = html5lib.parse(html)
        tree.name
    stop = time.time()
    print stop - start, "s"


if __name__ == '__main__':
    main()
