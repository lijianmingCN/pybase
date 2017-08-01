# -*- coding: utf-8 -*-
#28.7. contextlib — Utilities for with-statement contexts

from contextlib import contextmanager


@contextmanager
def make_context():
    print 'enter'
    try:
        yield {}
    except RuntimeError, err:
        print 'error', err
    finally:
        print 'exit'


with make_context() as value:
    print value