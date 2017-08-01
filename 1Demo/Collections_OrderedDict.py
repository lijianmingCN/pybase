# -*- coding: utf-8 -*-
from collections import OrderedDict
# regular unsorted dictionary
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
# dictionary sorted by key
print OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# dictionary sorted by value
print OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# dictionary sorted by length of the key string
print OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))





