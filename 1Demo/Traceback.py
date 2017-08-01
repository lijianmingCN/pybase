# -*- coding: utf-8 -*-

import sys, traceback

def exception1():
    try:
        1/0
    except:
        traceback.print_exc(file=sys.stdout)

def exception2():
    try:
        l = []
        l[1]
    except:
        traceback.print_exc(file=sys.stdout)

exception1()
exception2()