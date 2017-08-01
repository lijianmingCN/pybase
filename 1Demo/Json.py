# -*- coding: utf-8 -*-
import json

str = ['foo', {'bar': ('baz', None, 1.0, 2)}]
encode = json.dumps(str)
print encode
decode = json.loads(encode)
print decode
